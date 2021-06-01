#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.wait_state import WaitState
from pickit_flexbe_flexbe_states.message_state import MessageState
from pickit_flexbe_flexbe_states.pickit_capture_image_state import PickitCaptureImageState
from pickit_flexbe_flexbe_states.pickit_get_object_keys_state import PickitGetObjectKeysState
from pickit_flexbe_flexbe_states.pickit_load_product_state import PickitLoadProductState
from pickit_flexbe_flexbe_states.pickit_load_setup_state import PickitLoadSetupState
from pickit_flexbe_flexbe_states.pickit_process_image_state import PickitProcessImageState
from pickit_flexbe_flexbe_states.pickit_select_object_state import PickitSelectObjectState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 30 2021
@author: Gerard Harkema
'''
class pickit_demo_capture_image_and_process_imageSM(Behavior):
	'''
	Demo of a pickit application
	'''


	def __init__(self):
		super(pickit_demo_capture_image_and_process_imageSM, self).__init__()
		self.name = 'pickit_demo_capture_image_and_process_image'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1237 y:42, x:557 y:564
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.index = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:423 y:175
			OperatableStateMachine.add('CaptureImage',
										PickitCaptureImageState(),
										transitions={'continue': 'ProcessImage', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1027 y:374
			OperatableStateMachine.add('GetObjectKeys',
										PickitGetObjectKeysState(),
										transitions={'continue': 'object_pick_tf', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'object': 'object', 'object_tf': 'object_tf', 'object_pick_tf': 'object_pick_tf', 'object_post_pick_tf': 'object_post_pick_tf'})

			# x:27 y:174
			OperatableStateMachine.add('LoadProduct',
										PickitLoadProductState(product_file_name="cylinder"),
										transitions={'continue': 'LoadSetup', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:227 y:174
			OperatableStateMachine.add('LoadSetup',
										PickitLoadSetupState(setup_file_name="application_01"),
										transitions={'continue': 'CaptureImage', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1027 y:267
			OperatableStateMachine.add('Object',
										MessageState(),
										transitions={'continue': 'GetObjectKeys'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'object'})

			# x:811 y:172
			OperatableStateMachine.add('ObjectArrayMessage',
										MessageState(),
										transitions={'continue': 'SelectObject'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'object_array'})

			# x:627 y:174
			OperatableStateMachine.add('ProcessImage',
										PickitProcessImageState(),
										transitions={'continue': 'ObjectArrayMessage', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'object_array': 'object_array', 'number_of_objects': 'number_of_objects'})

			# x:1027 y:174
			OperatableStateMachine.add('SelectObject',
										PickitSelectObjectState(),
										transitions={'continue': 'Object', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'object_array': 'object_array', 'index': 'index', 'object': 'object'})

			# x:681 y:341
			OperatableStateMachine.add('Wait',
										WaitState(wait_time=1),
										transitions={'done': 'CaptureImage'},
										autonomy={'done': Autonomy.Off})

			# x:1032 y:460
			OperatableStateMachine.add('object_pick_tf',
										MessageState(),
										transitions={'continue': 'Wait'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'object_pick_tf'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
