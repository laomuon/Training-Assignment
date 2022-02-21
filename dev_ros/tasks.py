#!/usr/bin/env python3
from invoke import task

@task
def build(ctx):
    print("Build and copy the two ROS packages in intall mode")
    ctx.run("docker-compose -f ~/Training-Assignment/dev_ros/dev_ros.yaml build ros_service")

@task(build)
def run(ctx):
    print("Run the image")
    ctx.run("docker run -d --name my_container super-ros-node")


@task
def stop(ctx):
    print("Stop the container")
    ctx.run("docker stop my_container")

@task(stop)
def clean(ctx):
    print("Clean up")
    ctx.run("docker rm my_container")

@task
def debug(ctx):
    print("Go inside the container")
    ctx.run("docker exec -it my_container bash")
