#!/usr/bin/env bash

set -e

git --version
git submodule update --init --recursive

sudo apt-get install ros-catkin # for trusty dist
./resolve_mavros.sh

catkin build
