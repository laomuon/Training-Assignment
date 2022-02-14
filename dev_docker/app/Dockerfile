FROM ubuntu:18.04
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update \
    && apt-get -y  install python python-pip \
    && apt-get -y --no-install-recommends install python-tk \
    && pip install matplotlib 