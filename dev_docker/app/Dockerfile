FROM ubuntu:18.04
RUN mkdir /repo
WORKDIR /repo
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update \
    && apt-get -y  install python python-pip \
    && apt-get -y --no-install-recommends install python-tk \
    && pip install matplotlib
COPY . .
RUN chmod +x /repo/start.sh
CMD ["/repo/start.sh"]

#CMD ["python", "-i" ,"/repo/app.py"]
#CMD ["/bin/bash","-c", "trap \"\" INT; while [ true ]; do sleep 1; done;"]

#CMD python -i /repo/app.py; trap\ "\" INT; while [true];do sleep 1;done