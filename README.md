# PISS
Всеки Сървис ще се казва с името на някой древногръцки Бог

* A - Hermes - бога на съобщенията(защото праща съобщения)
* Б - Dyonysus - бог на събирането на реколтата(защото събира инфото от съобщенията и прави нещо с тях)
* В - Apollo - бога на знанията(защото е базата данни)

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

## Setup Hermes
* cd Hermes
* ./run.sh

## Setup vizualizations in grafana
* open influxdb -> localhost:8083
* check if there are any entries -> select * from "bus_data"

* open grafana -> localhost:3000 -> admin admin
* settings -> data sources -> new data source -> influxdb
* see set_up_influx_in_grafana.png in PISS for more info

TODO: explain with pics how to create the needed visualizations