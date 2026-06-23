import unittest

from audit_ontology_pipeline import parse_spo, extract_vocab_terms


class TestParseSpoFimDeFrase(unittest.TestCase):
    def test_predicado_no_final_da_frase_e_reconhecido(self):
        # Achado 3: antes do fix, a busca exigia espaço depois do predicado e
        # caía no fallback (2a palavra da frase) quando o predicado fechava a sentença.
        subj, pred, obj = parse_spo("O Item X deve_ser_validado", canonical_predicates=set())
        self.assertEqual(pred, "deve_ser_validado")
        self.assertEqual(subj, "O Item X")

    def test_predicado_no_meio_da_frase_continua_funcionando(self):
        subj, pred, obj = parse_spo("A Quadra de Jogo possui_status TERMO_CANÔNICO", canonical_predicates={"possui_status"})
        self.assertEqual(pred, "possui_status")
        self.assertEqual(subj, "A Quadra de Jogo")
        self.assertEqual(obj, "TERMO_CANÔNICO")


class TestVocabSubclasseDe(unittest.TestCase):
    def test_superclasse_via_e_subclasse_de_entra_no_vocabulario(self):
        # Achado 4: faltava o padrão é_subclasse_de na extração de vocab_terms,
        # deixando superclasses (ex: "Penalidade") fora do vocabulário válido.
        vocab_terms = extract_vocab_terms("Suspensão é_subclasse_de Penalidade.")
        self.assertIn("Penalidade", vocab_terms)
        self.assertIn("Suspensão", vocab_terms)


class TestRequiredNormalizaConvencao(unittest.TestCase):
    def test_termo_com_espaco_satisfaz_required_com_underscore(self):
        # Achado 5: a lista "required" usa underscore_case, mas o vocabulário é
        # escrito em linguagem natural com espaços — sem normalização, o check
        # nunca reconhecia um termo já declarado.
        vocab_terms = extract_vocab_terms("Especialista é_um Papel Tático.")
        self.assertIn("Papel_Tático", vocab_terms)


if __name__ == "__main__":
    unittest.main()
