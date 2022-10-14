# Cloud Computing Course at the Uppsala University

## Create VM and start RabbitMQ server

sudo apt-get install rabbitmq-server
### start server
sudo rabbitmq-server
### start monitoring flower
celery -A proj flower


rabbitmqctl add_user test test
rabbitmqctl set_user_tags test administrator
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"


## Deploy celery node at the SNIC data center (repeat this process if you need more worker nodes)
python3 deploy_worker.py

