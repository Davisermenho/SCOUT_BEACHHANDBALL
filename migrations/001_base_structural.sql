BEGIN IMMEDIATE;

CREATE TABLE IF NOT EXISTS schema_migrations (
  filename TEXT PRIMARY KEY,
  checksum_sha256 TEXT NOT NULL,
  applied_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS audit_log (
  id INTEGER PRIMARY KEY,
  entity_name TEXT NOT NULL,
  record_id TEXT NOT NULL,
  operation TEXT NOT NULL CHECK (
    operation IN (
      'insert',
      'update',
      'activate',
      'deactivate',
      'backup',
      'restore',
      'migration'
    )
  ),
  changed_at TEXT NOT NULL,
  before_state_json TEXT NULL,
  after_state_json TEXT NULL,
  reason TEXT NOT NULL,
  session_id TEXT NOT NULL,
  CHECK (
    before_state_json IS NOT NULL OR after_state_json IS NOT NULL
  )
);

CREATE INDEX IF NOT EXISTS audit_log_entity_record_idx
  ON audit_log (entity_name, record_id);

CREATE INDEX IF NOT EXISTS audit_log_changed_at_idx
  ON audit_log (changed_at);

CREATE TABLE IF NOT EXISTS athletes (
  id INTEGER PRIMARY KEY,
  full_name TEXT NOT NULL CHECK (length(trim(full_name)) > 0),
  nickname TEXT NULL,
  status TEXT NOT NULL DEFAULT 'active' CHECK (
    status IN ('active', 'inactive')
  ),
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS athletes_status_idx
  ON athletes (status);

CREATE TABLE IF NOT EXISTS competitions (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL CHECK (length(trim(name)) > 0),
  season TEXT NOT NULL CHECK (length(trim(season)) > 0),
  status TEXT NOT NULL DEFAULT 'active' CHECK (
    status IN ('active', 'inactive')
  ),
  location TEXT NULL,
  start_date TEXT NULL,
  end_date TEXT NULL
);

CREATE INDEX IF NOT EXISTS competitions_status_idx
  ON competitions (status);

CREATE TABLE IF NOT EXISTS opponents (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL CHECK (length(trim(name)) > 0),
  status TEXT NOT NULL DEFAULT 'active' CHECK (
    status IN ('active', 'inactive')
  ),
  city TEXT NULL,
  notes TEXT NULL
);

CREATE INDEX IF NOT EXISTS opponents_status_idx
  ON opponents (status);

COMMIT;
