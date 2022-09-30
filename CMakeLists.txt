cmake_minimum_required(VERSION 2.8.3)
project(rosmc_interface_msgs)

find_package(catkin REQUIRED COMPONENTS
    message_generation
    std_msgs
    geometry_msgs
    visualization_msgs
)

catkin_python_setup()

add_message_files(
    FILES
    Action.msg
    ActionContent.msg
    ActionStatus.msg
    AgentActions.msg
    AgentStatus.msg
    SyncIDs.msg
)

add_service_files(
    FILES
    Mission.srv
    RegisterToServer.srv
    TriggerMissionExecutor.srv
    UpdateActionStatus.srv
)

generate_messages(
    DEPENDENCIES std_msgs geometry_msgs visualization_msgs
)

catkin_package(
    CATKIN_DEPENDS std_msgs geometry_msgs message_runtime
    DEPENDS
    INCLUDE_DIRS
    LIBRARIES
)

install(PROGRAMS
  scripts/advertise_fake_mcg_services.py
  #scripts/advertise_mission_service.py
  #scripts/advertise_trigger_mission_executor_service.py
  #scripts/call_mission_service.py
  #scripts/call_trigger_mission_executor_service.py
  DESTINATION
  ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# Install config and rafcon files so that it can be accessed by `cissy run` and `conan install`
#install(DIRECTORY rafcon
#  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
#  USE_SOURCE_PERMISSIONS
#)
