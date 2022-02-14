This is the workspace for the dev_docker training module
alpine will be used as the Linux image
To launch the container:
- sudo docker-compose -f dev_docker.yaml build service-main
Building service-main
- sudo docker run -d -e DISPLAY=:0 --net host my_training_image