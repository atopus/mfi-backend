FROM python:3.10
ENV PYTHODONTWRITEBYCODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . ./

RUN chmod +x ./deploy/run.sh
RUN pip install --no-cache-dir -r requirements.txt

# ENTRYPOINT ["/bin/sh", "migrate.sh"]