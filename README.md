# Cloud Computing Course at the Uppsala University

## Create VM and start RabbitMQ server

sudo apt-get install rabbitmq-server
### start server
sudo rabbitmq-server

rabbitmqctl add_user test test

rabbitmqctl set_user_tags test administrator

rabbitmqctl set_permissions -p / test ".*" ".*" ".*"


### start monitoring flower
celery -A proj flower

---
## Deploy celery node at the SNIC data center (repeat this process if you need more worker nodes)
python3 deploy_worker.py

---
## Open Jupyter Notebook
Excetue count_pronouns() function and enjoy how celery workers are executing the queue tasks in the Rabbitmq server. 

