/*
 * Copyright 2018, Pick-it NV.
 * All rights reserved.
 */
#ifndef IM_PICKIT_MSGS_COMMON_H
#define IM_PICKIT_MSGS_COMMON_H

namespace im_pickit_msgs {
  /// Frame id being used for the robot's base frame.
  static const char ROBOT_BASE_FRAME_ID[] = "pickit/robot_base";
  /// Frame id being used for the Pick-it reference frame.
  static const char PICKIT_REFERENCE_FRAME_ID[] = "pickit/reference";
  /// Frame id being used for the robot's end-effector frame.
  static const char ROBOT_EE_FRAME_ID[] = "pickit/robot_ee";
}

#endif  // IM_PICKIT_MSGS_COMMON_H
