# MiniProject - Parallel Airfoil Simulations with Distributed Task Queue
## Prerequisite
1. Create a new VM, on this VM... 
2. Install the OpenStack client for Ubuntu:   apt install python3-openstackclient
3. Download the Runtime Configuration (RC) file from the SSC site (Project->API Access->Download OpenStack RC File (Identity API v3)). 
4. Show the contents of the file using cat. List the environment variables using env 
5. Execute the script using source. List the environment variables again, to show the new ones which are used by the client.  
6. git clone https://github.com/timbolo6/cloudcomputing.git
7. Generate your desired mesh files with ./runme.sh 0 30 10 200 3
8. Read README of airfoil 
9. or use Snapshot of wywiol-project

## Get started
- cd cloudcomputing/mini-project-celery/
- docker compose up --force-recreate

## Infos
- [IP]:8888 => Jupiter Notebook
- [IP]:5555 => Flower Monitoring
  
## Deploy celery node at the SNIC data center (repeat this process if you need more worker nodes)
- cd cloudcomputing/mini-project-celery/deployWorker
- python3 deploy_worker.py

