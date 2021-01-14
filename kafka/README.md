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

docker run -d -p 8083:8083 -p 8086:8086 --expose 8090 --expose 8099 tutum/influxdb 
http://localhost:8083 - InfluxDB PISS_DB is already created

docker run -d --name grafana -p 8080:80 -e INFLUXDB_HOST=localhost -e INFLUXDB_PORT=8086 -e INFLUXDB_NAME=mydata -e INFLUXDB_USER=root -e INFLUXDB_PASS=root tutum/grafana

http://localhost:8080 Grafana dashboard

## Run client for apollo
./run_apollo_client.sh