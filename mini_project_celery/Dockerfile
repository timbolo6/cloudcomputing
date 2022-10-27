FROM quay.io/fenicsproject/stable:current

RUN echo "hello world"
RUN apt update -y && apt upgrade -y
#RUN sudo apt-get install update
RUN sudo apt-get install gmsh -y
RUN sudo apt install python-numpy -y
#Install JupyterNotebook
RUN sudo apt install python3-pip -y
RUN sudo pip install notebook 
RUN sudo pip install celery 
#RUN jupyter notebook --ip=* --no-browser --allow-root
# Setup airfoil program
#WORKDIR /murtazo/navier_stokes_solver/src 
#RUN ./compile_forms
#RUN cd ..
#RUN cmake
#RUN make -j 2

# Create meshes
#WORKDIR /murtazo/cloudnaca
#RUN ./runme.sh 0 30 10 200 3

# Convert msh to xml

#RUN ./airfoil 10 0.0001 10. 1 ../cloudnaca/msh/..xml
