-- Optional initial database setup or extension activation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Verification notice on container startup
DO $$
BEGIN
    RAISE NOTICE 'DevTrack PostgreSQL database initialized successfully.';
END
$$;