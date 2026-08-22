FROM postgres:15-alpine

# Set default database credentials
ENV POSTGRES_DB=devtrack_db
ENV POSTGRES_USER=shashikant
ENV POSTGRES_PASSWORD=12345

# Any .sql or .sh files copied here execute automatically on first initialization
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432