FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

COPY ./DDL.sql /docker-entrypoint-initdb.d/

COPY ./DML.sql /docker-entrypoint-initdb.d/

COPY ./DQL.sql /docker-entrypoint-initdb.d/