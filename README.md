# PISS
Всеки Сървис ще се казва с името на някой древногръцки Бог

* A - Hermes - бога на съобщенията(защото праща съобщения)
* Б - Dyonysus - бог на събирането на реколтата(защото събира инфото от съобщенията и прави нещо с тях)
* В - Apolo - бога на знанията(защото е базата данни)

## Setup grafana and influxdb
* cd `some random terminal`

* docker rm influxdb grafana

* docker run -d -p 8083:8083 -p 8086:8086 \
  -e PRE_CREATE_DB="wadus" \
  --expose 8090 --expose 8099 \
  --name influxdb \
  tutum/influxdb

* docker run -d -p 3000:3000 \
  --link influxdb:influxdb \
  --name grafana \
  grafana/grafana

## Setup kafka
* cd PISS/kafka
* ./utils/run_zookeeper.sh
* ./utils/run_kafka.sh
* ./utils/create_kafka_topic.sh
* ./utils/get_topic_info.sh

## Setup Apollo
* cd PISS/Apollo/setup
* docker-compose up
* ./install_go_dependencies.sh
* cd Apollo
* go run .

## Setup Dyonysus
* cd Dyonysus
* pip install -r requirements.txt
* ./run.sh

You may need to setup the proto messages, but you shouldn't need to:
* cd PISS/Dyonysus/grpc/messages
* python -m grpc_tools.protoc --proto_path=. ./apollo.proto --python_out=. --grpc_python_out=.

#### Setup proto messages

## Setup Hermes
* cd Hermes
* ./run.sh
