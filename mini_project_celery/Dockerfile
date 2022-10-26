FROM quay.io/fenicsproject/stable:current
RUN echo "hello world"
RUN apt-get install update
RUN apt-get install gmsh

WORKDIR /murtazo/navier_stokes_solver/src 
RUN ./compile_forms
RUN cd ..
RUN cmake
RUN make -j 2


