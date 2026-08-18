FROM postgres:15-alpine

# Set default database credentials
ENV POSTGRES_DB=devtrack_db
ENV POSTGRES_USER=devtrack_user
ENV POSTGRES_PASSWORD=devtrack_password

# Any .sql or .sh files copied here execute automatically on first initialization
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432