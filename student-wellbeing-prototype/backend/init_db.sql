CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS vector;

-- Users
CREATE TABLE IF NOT EXISTS users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  hashed_password TEXT,
  role TEXT NOT NULL DEFAULT 'student',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
  consent_given BOOLEAN DEFAULT false
);

-- Student profile
CREATE TABLE IF NOT EXISTS student_profiles (
  user_id UUID PRIMARY KEY REFERENCES users(id),
  full_name TEXT,
  program TEXT,
  year INTEGER,
  gpa NUMERIC(3,2),
  attendance_percent NUMERIC(5,2),
  last_activity TIMESTAMPTZ
);

-- Chat messages
CREATE TABLE IF NOT EXISTS chat_messages (
  id BIGSERIAL PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  msg TEXT,
  sentiment JSONB,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Embeddings (pgvector)
CREATE TABLE IF NOT EXISTS embeddings (
  id BIGSERIAL PRIMARY KEY,
  source_type TEXT,
  source_id TEXT,
  embedding vector(1536),
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Risk
CREATE TABLE IF NOT EXISTS risk_scores (
  id BIGSERIAL PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  score FLOAT,
  model_version TEXT,
  features JSONB,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Peer matches
CREATE TABLE IF NOT EXISTS peer_match (
  id BIGSERIAL PRIMARY KEY,
  mentee_id UUID REFERENCES users(id),
  mentor_id UUID REFERENCES users(id),
  matched_at TIMESTAMPTZ DEFAULT now(),
  score FLOAT
);
