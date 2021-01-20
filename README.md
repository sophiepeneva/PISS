# PISS
Всеки Сървис ще се казва с името на някой древногръцки Бог

* A - Hermes - бога на съобщенията(защото праща съобщения)
* Б - Dyonysus - бог на събирането на реколтата(защото събира инфото от съобщенията и прави нещо с тях)
* В - Apollo - бога на знанията(защото е базата данни)

## Setup Apollo
* cd PISS/Apollo/setup
* docker-compose up
* ./install_go_dependencies.sh
* cd Apollo
* ./run.sh

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

* for adding visualizations and the necessary queries look at images:
 * in_out_line_chart.png
 * people_int_out_stat.png
 * people_on_station.png
 * people_per_bus_heatmap.png
 * people_per_bus_line_chart.png
* for adding grafana variables to filter charts look at images:
 * variables_settings.png
 * bus_num_var_settings.png
* the result should look like grafana_dashboard.png