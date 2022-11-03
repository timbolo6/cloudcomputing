FROM quay.io/fenicsproject/stable:current

RUN echo "Contextualize Celery Worker Node"
RUN apt update -y && apt upgrade -y
RUN sudo apt-get install gmsh -y
RUN sudo apt install python-numpy -y
#Install JupyterNotebook
RUN sudo apt install python3-pip -y
RUN sudo pip install notebook 
RUN sudo pip install celery 

#TODO
# Setup airfoil program
#WORKDIR /murtazo/navier_stokes_solver/src 
#RUN ./compile_forms
#RUN cd ..
#RUN cmake
#RUN make -j 2
# Create meshes
#WORKDIR /murtazo/cloudnaca
#RUN ./runme.sh 0 30 10 200 3

# START CELERY WORKER
ENTRYPOINT ["celery"]
CMD ["-A","proj","worker","--loglevel=INFO", "-n","worker@%h"] 
