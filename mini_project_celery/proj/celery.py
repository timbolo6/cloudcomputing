from celery import Celery
import subprocess
import json
# Celery configuration
CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
CELERY_RESULT_BACKEND = 'rpc://'
# Initialize Celery
app = Celery('celery', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@app.task
def startSimulation(filename,input_path):
    #get path for filename and corresponding .xml file
    xmlfilename = input_path + filename.split(".")[0]+".xml"
    filename_path = input_path + filename
    
    #Task 1 convert msh to xml by dolfin-convert <msh> <xml>
    #!dolfin-convert $filename_path $xmlfilename
    subprocess.run(["dolfin-convert", filename_path, xmlfilename],check=True)
    #Task 2 run navier_stokes_solver by ./airfoil 10 0.0001 10. 1 file
    #! ../murtazo/navier_stokes_solver/airfoil 10 0.00001 10. 1 $xmlfilename
    subprocess.run(["../murtazo/navier_stokes_solver/airfoil", "10","0.0001","10.","1", xmlfilename],check=True)
    #Task3 getResults by Tail –n 1 drag_ligt.m
    #output = !tail -n 1  ../murtazo/navier_stokes_solver/results/drag_ligt.m 
    output =  subprocess.run(["tail", "-n","1", "../murtazo/navier_stokes_solver/results/drag_ligt.m"],check=True, stdout=subprocess.PIPE, universal_newlines=True)
    result = {"filename": filename, "lift": output.stdout.split("\t")[1], "drag":output.stdout.split("\t")[2].slit("\n")[0]}
    return json.dumps(result)

if __name__ == '__main__':
    app.start()
