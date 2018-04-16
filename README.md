# corvus
Redbird Robotic's flagship autonomous aerial drone.


# Startup instructions

From a remote machine, do the following:

```sh
# ssh into vehicle
ssh <vehicle_username>@<vehicle_address>

# clone the flight repo
git clone https://github.com/redbirdrobotics/test-catkin-ws
cd test-catkin-ws

# build the ros project(s)
catkin build

# source the generated env variables
source devel/setup.bash

# launch the launchfile
roslaunch redbird_m7a_vehicle startup.launch

# serve the desired flight to the vehicle (this corresponds to a programmed 
#   "flight", discoverable by the "flight_director".)
rosservice call /redbird/flight_director/start_flight "takeoff_land"
```

Having any issues?
try opening a new terminal any sourcing the environment variables again (from a 
properly built catkin workspace) using `source devel/setup.bash`.



# Encountered build issue and solutions

+ `warning: libboost_system.so.1.58.0, needed by /opt/ros/kinetic/lib/libroscpp.so, may conflict with libboost_system.so.1.61.0`

solved with:
```sh
wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
chmod +x install_geographiclib_datasets.sh # make sure we have permissions
./install_geographiclib_datasets.sh
```



# How to contribute: 
git clone https://github.com/redbirdrobotics/corvus
git checkout -b [sim|loc|flight|controlpanel]dev # depending on your subteam

