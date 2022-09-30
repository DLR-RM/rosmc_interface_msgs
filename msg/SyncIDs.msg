# the sync_ids have to map to the action_id(s) of the Action.msg
# the sync_ids have to format [lru1_action_id, lru2_action_id, ardea_action_id]
# if an agent should not be part in the synchronization its id is simply None
# if there is no own action for an agent that should be synchronized but if the agent just want to synchronize
#     to the actions of other agents then the action_id must be "WAIT_FOR_OTHER_ACTIONS"
string[] sync_ids