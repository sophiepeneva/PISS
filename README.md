# PISS

Имаме идея това да общо репо на всичките сървиси
Всеки Сървис ще се казва с името на някой древногръцки Бог

* A - Hermes - бога на съобщенията(защото праща съобщения)
* Б - Dyonysus - бог на събирането на реколтата(защото събира инфото от съобщенията и прави нещо с тях)
* В - Apolo - бога на знанията(защото е базата данни)

## First see kafka README

## Setup grafana and influxdb

docker run -d -p 8083:8083 -p 8086:8086 \
  -e PRE_CREATE_DB="wadus" \
  --expose 8090 --expose 8099 \
  --name influxdb \
  tutum/influxdb

docker run -d -p 3000:3000 \
  --link influxdb:influxdb \
  --name grafana \
  grafana/grafana

* grafana -> localhost:3000

## Run client for apollo
./run_apollo_client.sh

## Build proto message files
cd Dyonysus/grpc/messages
python -m grpc_tools.protoc --proto_path=. ./Bus.proto --python_out=. --grpc_python_out=.

## Run whole pipeline
* first we run kafka
* run apollo server
* run influxdb and grafana
* run kafka subscriber -> cd PISS/Dyonysus -> ./run_kafka_subscriber.sh
* cd PISS/Hermes -> ./run.sh
* now the data should be in influx and can be graphed in grafana