FROM mysql/mysql-server:8.0

ENV MYSQL_DATABASE tokens
ENV MYSQL_ROOT_PASSWORD amezzon_token
EXPOSE 3306

COPY ./sql-scripts/ /docker-entrypoint-initdb.d/
