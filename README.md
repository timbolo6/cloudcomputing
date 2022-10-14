# Cloud Computing Course at the Uppsala University

## Prerequisite
1. Create a new VM, on this VM... 
2. Install the OpenStack client for Ubuntu:   apt install python3-openstackclient
3. Download the Runtime Configuration (RC) file from the SSC site (Project->API Access->Download OpenStack RC File (Identity API v3)). 
4. Show the contents of the file using cat. List the environment variables using env 
5. Execute the script using source. List the environment variables again, to show the new ones which are used by the client.  
6. git clone https://github.com/timbolo6/cloudcomputing.git

## Start RabbitMQ server
sudo apt-get install rabbitmq-server
### start server
sudo rabbitmq-server
### add new user
rabbitmqctl add_user test test

rabbitmqctl set_user_tags test administrator

rabbitmqctl set_permissions -p / test ".*" ".*" ".*"


### start monitoring flower
pip install flower
celery -A proj flower

---
## Deploy celery node at the SNIC data center (repeat this process if you need more worker nodes)
python3 deploy_worker.py

---
## Open Jupyter Notebook
Excetue count_pronouns() function and enjoy how celery workers are executing the queue tasks in the Rabbitmq server. 

