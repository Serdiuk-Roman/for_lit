FROM python:3.6

COPY . /data/backend/
WORKDIR /data/backend/

RUN pip install -r requirements.txt --no-cache-dir

RUN  chmod  +x ./bin/entry-point.sh

EXPOSE 8000

ENTRYPOINT ["./bin/entry-point.sh"]
