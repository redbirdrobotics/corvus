#!/usr/bin/env bash

set -e

git submodule update --init --recursive
catkin build

# source the generated ros env variables
source devel/setup.bash

