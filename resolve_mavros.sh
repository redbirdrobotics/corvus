#!/usr/bin/env bash

set -e

## mavros (and mavlink) (see https://github.com/mavlink/mavros/blob/master/mavros/README.md#binary-installation-deb)
sudo apt-get update
rosdep update
sudo apt-get install ros-kinetic-mavros ros-kinetic-mavros-extras
sudo apt-get install python-catkin-tools python-rosinstall-generator -y

## geographical lib datasets (for mavros)
wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
chmod +x install_geographiclib_datasets.sh # make sure we have permissions
sudo ./install_geographiclib_datasets.sh
rm install_geographiclib_datasets.sh
