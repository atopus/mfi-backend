FROM python:3-alpine
ENV PYTHODONTWRITEBYCODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . ./
RUN chmod +x migrate.sh
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
        uwsgi-python3 \
		libc-dev \
		linux-headers;
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/bin/sh", "migrate.sh"]
