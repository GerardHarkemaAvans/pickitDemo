cmake_minimum_required(VERSION 2.8.3)
project(im_pickit_msgs)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  message_generation
  geometry_msgs
  sensor_msgs
  shape_msgs
  std_msgs
  std_srvs
  visualization_msgs
)

################################################
## Declare ROS messages, services and actions ##
################################################

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  BlacklistedPick.msg
  BlacklistedPickArray.msg
  Object.msg
  ObjectArray.msg
  ObjectModel.msg
  Reliability.msg
  ReliabilityValue.msg
  StatusError.msg
  StatusInvalid.msg
  StatusUnpickable.msg
  SubStatus.msg

  FolderContent.msg
  File.msg
  SubfolderContent.msg

  Model.msg
  ModelsData.msg
  ObjectPickFrame.msg
  ObjectPickFrames.msg
  ObjectPickFrameSymmetry.msg
  TeachXDModelsData.msg

  BoundingBox.msg
  ColorRangeRGB.msg
  ColorRangeHSV.msg
  CalibrationStatus.msg
  SnapshotStatus.msg
  MonitoringEvent.msg

  RegionOfInterest.msg

  PointIndices.msg
  PointCloud2Array.msg
  ToolModels.msg
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  AddBlacklistedPick.srv
  AddMeshTool.srv
  AddShapeModel.srv
  BackupConfigurations.srv
  CaptureImage.srv
  CheckForObjects.srv
  ConstructTeachXdModel.srv
  CopyConfiguration.srv
  CreateConfiguration.srv
  DetectTeachXdBoxMasks.srv
  EditConfigurationFiles.srv
  IntArg.srv
  LoadConfig.srv
  LoadSnapshot.srv
  ModelData.srv
  ModelXdData.srv
  ProcessImage.srv
  RestoreConfigurations.srv
  SaveActiveConfiguration.srv
  SaveCameraSettings.srv
  SaveConfiguration.srv
  SaveSnapshot.srv
  SetObjectPickFrames.srv
  SetShapePickFrames.srv
  SetTransform.srv
  SetToolModels.srv
  StrArg.srv
  TeachFromCad.srv
  TeachRoi.srv
)

add_action_files(
  FILES
  GetReferenceFrame.action
)

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   actionlib_msgs geometry_msgs sensor_msgs shape_msgs std_msgs std_srvs visualization_msgs
 )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
   INCLUDE_DIRS include
#  LIBRARIES im_pickit_msgs
   CATKIN_DEPENDS actionlib_msgs message_runtime geometry_msgs sensor_msgs std_msgs std_srvs
#  DEPENDS system_lib
)

install(DIRECTORY include/${PROJECT_NAME}/
        DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION})
