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
from pickit_flexbe_flexbe_states.pickit_check_for_objects_state import PickitCheckForObjectsState
from pickit_flexbe_flexbe_states.pickit_get_object_keys_state import PickitGetObjectKeysState
from pickit_flexbe_flexbe_states.pickit_load_product_state import PickitLoadProductState
from pickit_flexbe_flexbe_states.pickit_load_setup_state import PickitLoadSetupState
from pickit_flexbe_flexbe_states.pickit_select_object_state import PickitSelectObjectState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 30 2021
@author: Gerard Harkema
'''
class pickit_demoSM(Behavior):
	'''
	Demo of a pickit application
	'''


	def __init__(self):
		super(pickit_demoSM, self).__init__()
		self.name = 'pickit_demo'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1237 y:42, x:583 y:411
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.index = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:27 y:174
			OperatableStateMachine.add('LoadProduct',
										PickitLoadProductState(product_file_name="cylinder"),
										transitions={'continue': 'LoadSetup', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:827 y:174
			OperatableStateMachine.add('GetObjectKeys',
										PickitGetObjectKeysState(),
										transitions={'continue': 'Wait', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'object': 'object', 'object_tf': 'object_tf', 'object_pick_tf': 'object_pick_tf', 'object_post_pick_tf': 'object_post_pick_tf'})

			# x:227 y:174
			OperatableStateMachine.add('LoadSetup',
										PickitLoadSetupState(setup_file_name="application_01"),
										transitions={'continue': 'CheckForObjects', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:627 y:174
			OperatableStateMachine.add('SelectObject',
										PickitSelectObjectState(),
										transitions={'continue': 'GetObjectKeys', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'object_array': 'object_array', 'index': 'index', 'object': 'object'})

			# x:649 y:30
			OperatableStateMachine.add('Wait',
										WaitState(wait_time=1),
										transitions={'done': 'CheckForObjects'},
										autonomy={'done': Autonomy.Off})

			# x:424 y:174
			OperatableStateMachine.add('CheckForObjects',
										PickitCheckForObjectsState(),
										transitions={'continue': 'SelectObject', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'object_array': 'object_array', 'number_of_objects': 'number_of_objects'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
