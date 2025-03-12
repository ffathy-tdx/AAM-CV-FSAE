cmake_minimum_required(VERSION 3.0.2)
project(yolov10_cone_detection)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  rospy
  sensor_msgs
  std_msgs
)

###################################
## catkin specific configuration ##
###################################
catkin_package()

###########
## Build ##
###########
# Since your node is Python-based, there's no C++ compilation here.

include_directories(
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

# 1. Install Python scripts (nodes) from the 'src/' folder
catkin_install_python(
  PROGRAMS
    src/yolo_cone_detection_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# 2. (Optional) Install launch/ folder so it’s accessible when the package is installed
install(
  DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

# 3. (Optional) Install weights/ folder so your .pt file is also installed
install(
  DIRECTORY weights/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/weights
)

# If you have other folders (config/, etc.), install them similarly.
