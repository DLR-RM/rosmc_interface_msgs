#!/usr/bin/env python

import rospy
from rosmc_interface_msgs.srv import RegisterToServer, RegisterToServerResponse, UpdateActionStatus, UpdateActionStatusResponse


def handle_register_to_server_request(req):
    print "Called handle_register_to_server_request"
    print req
    res = RegisterToServerResponse()
    res.success = True
    res.mission_server_namespace = rospy.get_namespace()
    return res


def handle_update_action_status_request(req):
    print "Called handle_update_action_status_request"
    print req
    return UpdateActionStatusResponse()


def mission_executor(agent_name):
    rospy.init_node(agent_name)
    # Use global service name only for registration
    rospy.Service('register_to_mission_server', RegisterToServer, handle_register_to_server_request)
    print "Ready to register ..."

    rospy.Service('update_action_status', UpdateActionStatus, handle_update_action_status_request)
    print "Ready to update action status ..."

    rospy.spin()


if __name__ == "__main__":
    mission_executor('register_to_server_node')
