cmake_minimum_required (VERSION 2.4.6)
include ($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

set (ROS_BUILD_TYPE RelWithDebInfo)
rosbuild_init ()
rosbuild_add_boost_directories ()

find_package(Eigen REQUIRED)
include_directories(${EIGEN_INCLUDE_DIRS})

set (EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

# Dynamic reconfigure
rosbuild_find_ros_package(dynamic_reconfigure)
include(${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake)
gencfg()

# ROS nodelet library
rosbuild_add_library (openni_deprecated src/nodelets/openni_nodelet.cpp)

# Node version of ROS driver
rosbuild_add_executable (openni_node src/nodes/openni_node.cpp)
