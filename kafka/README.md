# Kafka quickstart
This is everything you need.
https://kafka.apache.org/quickstart

The whole kafka is in the folder source 

*go to the source directory*

## Run kafka 
>> in separate terminals in the correct order

* ./run_zookeeper.sh
* ./run_kafka.sh

## Create topic and get topic info
* ./create_kafka_topic.sh
* ./get_topic_info.sh

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
from Dyonysus/grpc/messages exec
python -m grpc_tools.protoc --proto_path=. ./Bus.proto --python_out=. --grpc_python_out=.