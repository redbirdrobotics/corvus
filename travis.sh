#!/usr/bin/env bash

set -e

git --version
git submodule update --init --recursive

sudo apt-get install python-catkin-pkg
./resolve_mavros.sh

catkin build

