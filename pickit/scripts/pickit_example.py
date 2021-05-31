#!/usr/bin/env python
import rospy
from im_pickit_msgs.srv import LoadConfig, CheckForObjects
from im_pickit_msgs.msg import ObjectArray


if __name__ == "__main__":
  rospy.init_node("pickit_client")

  # Initialize ROS services.
  rospy.wait_for_service("/pickit/configuration/product/load")
  rospy.wait_for_service("/pickit/configuration/setup/load")
  rospy.wait_for_service("/pickit/check_for_objects")
  load_product_srv = rospy.ServiceProxy("/pickit/configuration/product/load", LoadConfig)
  load_setup_srv = rospy.ServiceProxy("/pickit/configuration/setup/load", LoadConfig)
  detect_srv = rospy.ServiceProxy("/pickit/check_for_objects", CheckForObjects)

  # Load initial configuration by their product & setup name.
  response = load_product_srv("cylinder", True)
  assert response.success, "Failed to load product config."
  response = load_setup_srv("application_01", True)
  assert response.success, "Failed to load setup config."

  # Continuously detect objects and move a robot arm to the first detected object pose.
  response = detect_srv()
  while response.objects.status == ObjectArray.STATUS_SUCCESS and response.objects.n_valid_objects > 0:
    rospy.loginfo("Detected {} objects".format(response.objects.n_valid_objects))
    first_object = response.objects.objects[0]

    # Note that object poses are expressed in the pickit/reference frame. You can use tf or one of
    # the transforms in the service reponse to transform them to your desired frame.
    object_pick_pose = first_object.object_pick_tf

    # Move robot arm to object pick pose
    # ...

    response = detect_srv()
