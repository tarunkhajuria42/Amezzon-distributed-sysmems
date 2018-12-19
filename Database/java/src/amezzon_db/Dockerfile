FROM mysql/mysql-server:8.0

ENV MYSQL_DATABASE amezzon
ENV MYSQL_USER root
ENV MYSQL_ROOT_PASSWORD amezzon_db
EXPOSE 3306

COPY ./sql-scripts/ /docker-entrypoint-initdb.d/

