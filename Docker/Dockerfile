FROM postgres:11
RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV POSTGRES_PASSWORD test_postgres
ENV POSTGRES_DB test_db
COPY *.sql /docker-entrypoint-initdb.d/