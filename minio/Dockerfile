FROM minio/minio:latest

RUN chmod -R 777 /usr/bin

#COPY ./minio /usr/bin/minio
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

VOLUME ["/data"]

CMD ["minio"]
