#!/usr/bin/env bash

set -e

# openssh-server
#
# why?
#    mavros expects the ability to enable an ssh connection with the ground 
#  station. openssh-server will permit ssh connection into this machine.
sudo apt-get install openssh-server

