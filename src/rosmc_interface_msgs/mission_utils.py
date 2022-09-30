#!/usr/bin/env python
"""
Utility functions used in High-level Mission Executor.
"""

gv_name_update_action = "update_action_status_request_list"


def append_update_action_status_request(self, gvm, req):
    # wait until global variable is set by update action status handler
    while not gvm.data_type_exist(gv_name_update_action):
        self.logger.warn("Global variable " + gv_name_update_action + " is not initialized yet. Wait for its initialization...")
        self.wait_for_interruption(0.1)
        if self.preempted:
            return -2
        if self.paused:
            self.wait_for_unpause()
            if self.preempted:
                return -2
    # Append request to global variable
    while True:
        if gvm.is_locked(gv_name_update_action):
            self.logger.warn("Global variable " + gv_name_update_action + " is locked. Wait for being unlocked...")
            self.wait_for_interruption(0.1)
            if self.preempted:
                return -2
            if self.paused:
                self.wait_for_unpause()
                if self.preempted:
                    return -2
        else:
            self.logger.info("Acquired lock of " + gv_name_update_action)
            access_key = gvm.lock_variable(key=gv_name_update_action, block=True)
            update_action_status_request_list = gvm.get_locked_variable(gv_name_update_action, access_key)
            update_action_status_request_list.append(req)
            gvm.set_locked_variable(key=gv_name_update_action, access_key=access_key,
                                    value=update_action_status_request_list)
            gvm.unlock_variable(key=gv_name_update_action, access_key=access_key)
            self.logger.info("Released lock of " + gv_name_update_action)
            break
