#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2021, Avans, University of applied science
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Delft University of Technology nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Gerard Harkema
# email: GA.Harkema@avans.nl
# Date: may 29, 2021
# Version: 1.0

import rospy
from im_pickit_msgs.srv import LoadConfig, CheckForObjects
from im_pickit_msgs.msg import ObjectArray
from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyActionClient

class PickitCheckForObjectsState(EventState):
  '''
  Captures the camera image and processing the image, resulting al list of detected defined objects

  #> object_array       ObjectArray   Array of the detected objects
  #> number_of_objects      int       Number of valid detected objects
  <= continue 					Given time has passed.
  <= failed 						Failed to load product file.

  '''

  def __init__(self):
    # Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
    super(PickitCheckForObjectsState, self).__init__(outcomes = ['continue', 'failed'], output_keys = ['object_array', 'number_of_objects'])


    # The constructor is called when building the state machine, not when actually starting the behavior.
    self.service_timeout = 5.0
    self.success = False
    self.service_up = False

    Logger.loginfo('Waiting for service...')
    try:
      rospy.wait_for_service('/pickit/check_for_objects', self.service_timeout)
    except rospy.ROSException, e:
      Logger.logwarn('Service not up')
      return
    
    self.detect_srv = rospy.ServiceProxy("/pickit/check_for_objects", CheckForObjects)
    self.service_up = True


  def execute(self, userdata):

    # This method is called when the state becomes active, i.e. a transition from another state to this one is taken.
    # It is primarily used to start actions which are associated with this state.

    if self.success:
      return 'continue'
    return 'failed' # One of the outcomes declared above.

  def on_enter(self, userdata):
    self.success = False
    
    if self.service_up:
      try:
        response = detect_srv()
      except rospy.ServiceException as exc:
        Logger.logwarn('Service did not process request: ' + str(exc))
        return
      if response.objects.status == ObjectArray.STATUS_SUCCESS:
        userdata.number_of_objects = response.objects.n_valid_objects
        userdata.object_array = response.objects.objects
        self.success = True
    

  def on_exit(self, userdata):
    # This method is called when an outcome is returned and another state gets active.
    # It can be used to stop possibly running processes started by on_enter.

    pass # Nothing to do in this example.


  def on_start(self):
    # This method is called when the behavior is started.
    # If possible, it is generally better to initialize used resources in the constructor
    # because if anything failed, the behavior would not even be started.

    # In this example, we use this event to set the correct start time.
    pass # Nothing to do in this example.


  def on_stop(self):
    # This method is called whenever the behavior stops execution, also if it is cancelled.
    # Use this event to clean up things like claimed resources.

    pass # Nothing to do in this example.
