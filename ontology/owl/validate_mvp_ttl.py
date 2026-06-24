#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

from rdflib import BNode, Graph, Namespace, RDF, RDFS, OWL, URIRef
from rdflib.collection import Collection


TTL_PATH = Path(__file__).with_name("scout_beachhandball_mvp.ttl")
HBP = Namespace("https://github.com/Davisermenho/SCOUT_BEACHHANDBALL/ontology/mvp#")
DCTERMS = Namespace("http://purl.org/dc/terms/")

EXPECTED_CLASSES = {
    "Papel_Tatico",
    "Papel_Regulamentar",
    "Funcao_Situacional",
    "Posicao_Espacial",
    "Especialista",
    "Goleiro",
}

BLOCKED_CLASSES = {
    "Gol",
    "Pontuacao",
    "Gol_Espetacular",
    "Gol_de_Giro",
    "Gol_Aereo",
    "Gol_Criativo",
    "Jogador_De_Linha",
    "Autor_Do_Gol",
    "Fundamento_Da_Pontuacao",
}

EXPECTED_OBJECT_PROPERTIES = {
    "tem_papel_tatico": "Papel_Tatico",
    "tem_papel_regulamentar": "Papel_Regulamentar",
    "executa_funcao_situacional": "Funcao_Situacional",
    "ocupa_posicao_espacial": "Posicao_Espacial",
}

EXPECTED_ONTOLOGY_ANNOTATIONS = {
    RDFS.label: 1,
    RDFS.comment: 1,
    DCTERMS.created: 1,
    DCTERMS.source: 1,
    OWL.versionInfo: 1,
}


def fail(errors: list[str]) -> int:
    for error in errors:
        print(f"ERROR: {error}")
    return 1


def ensure_annotation_count(
    graph: Graph, subject: URIRef, predicate: URIRef, minimum: int, errors: list[str]
) -> None:
    count = len(list(graph.objects(subject, predicate)))
    if count < minimum:
        errors.append(
            f"{subject} must have at least {minimum} value(s) for {predicate}, found {count}"
        )


def validate_all_disjoint_dimensions(graph: Graph, errors: list[str]) -> None:
    expected = {
        HBP.Papel_Tatico,
        HBP.Papel_Regulamentar,
        HBP.Funcao_Situacional,
        HBP.Posicao_Espacial,
    }

    for node in graph.subjects(RDF.type, OWL.AllDisjointClasses):
        members_node = graph.value(node, OWL.members)
        if isinstance(members_node, BNode):
            members = set(Collection(graph, members_node))
            if members == expected:
                return

    errors.append("Missing owl:AllDisjointClasses axiom for the four structural dimensions")


def main() -> int:
    graph = Graph()

    try:
        graph.parse(TTL_PATH, format="turtle")
    except Exception as exc:  # pragma: no cover - parse failure is the result
        print(f"ERROR: Turtle parse failed for {TTL_PATH}: {exc}")
        return 1

    errors: list[str] = []

    ontologies = list(graph.subjects(RDF.type, OWL.Ontology))
    if len(ontologies) != 1:
        errors.append(f"Expected exactly 1 owl:Ontology declaration, found {len(ontologies)}")
    else:
        ontology = ontologies[0]
        for predicate, minimum in EXPECTED_ONTOLOGY_ANNOTATIONS.items():
            ensure_annotation_count(graph, ontology, predicate, minimum, errors)

    datatype_properties = list(graph.subjects(RDF.type, OWL.DatatypeProperty))
    if datatype_properties:
        errors.append(
            "No owl:DatatypeProperty is allowed in this MVP scope, found: "
            + ", ".join(sorted(str(p) for p in datatype_properties))
        )

    for class_name in sorted(EXPECTED_CLASSES):
        class_uri = HBP[class_name]
        if (class_uri, RDF.type, OWL.Class) not in graph:
            errors.append(f"Missing expected class {class_name}")
            continue
        ensure_annotation_count(graph, class_uri, RDFS.label, 1, errors)
        ensure_annotation_count(graph, class_uri, RDFS.comment, 1, errors)
        ensure_annotation_count(graph, class_uri, DCTERMS.source, 1, errors)

    for class_name in sorted(BLOCKED_CLASSES):
        class_uri = HBP[class_name]
        if (class_uri, RDF.type, OWL.Class) in graph:
            errors.append(f"Blocked class present in MVP file: {class_name}")

    object_properties = {
        str(subject).split("#")[-1]
        for subject in graph.subjects(RDF.type, OWL.ObjectProperty)
        if str(subject).startswith(str(HBP))
    }
    expected_property_names = set(EXPECTED_OBJECT_PROPERTIES)
    extra_properties = sorted(object_properties - expected_property_names)
    if extra_properties:
        errors.append(
            "Unexpected owl:ObjectProperty in MVP file: " + ", ".join(extra_properties)
        )

    for property_name, range_name in sorted(EXPECTED_OBJECT_PROPERTIES.items()):
        property_uri = HBP[property_name]
        if (property_uri, RDF.type, OWL.ObjectProperty) not in graph:
            errors.append(f"Missing expected object property {property_name}")
            continue

        ensure_annotation_count(graph, property_uri, RDFS.label, 1, errors)
        ensure_annotation_count(graph, property_uri, RDFS.comment, 1, errors)
        ensure_annotation_count(graph, property_uri, DCTERMS.source, 1, errors)

        actual_ranges = set(graph.objects(property_uri, RDFS.range))
        expected_range = HBP[range_name]
        if actual_ranges != {expected_range}:
            errors.append(
                f"{property_name} must have exactly range {range_name}, found "
                + ", ".join(sorted(str(r) for r in actual_ranges))
            )

    if (HBP.Especialista, RDFS.subClassOf, HBP.Papel_Tatico) not in graph:
        errors.append("Especialista must be rdfs:subClassOf Papel_Tatico")

    if (HBP.Goleiro, RDFS.subClassOf, HBP.Papel_Regulamentar) not in graph:
        errors.append("Goleiro must be rdfs:subClassOf Papel_Regulamentar")

    if (HBP.Especialista, OWL.disjointWith, HBP.Goleiro) not in graph:
        errors.append("Especialista must be owl:disjointWith Goleiro")

    validate_all_disjoint_dimensions(graph, errors)

    if errors:
        return fail(errors)

    print(f"OK: {TTL_PATH} parsed and validated successfully")
    print(f"Triples: {len(graph)}")
    print(f"Classes: {len(EXPECTED_CLASSES)} expected and present")
    print(f"Object properties: {len(EXPECTED_OBJECT_PROPERTIES)} expected and present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
