uint8 IDLE = 0
uint8 SUCCESS = 1
uint8 FAILURE = 2
uint8 RUNNING = 3
uint8 PAUSED = 4
uint8 STOPPED = 5
uint8 RESUMED = 6
uint8 SYNCWAITING = 7
uint8 IDLE_SYNCHRONISED = 8

uint8 value
# placeholder for status specific information, e.g. the reason of failure
string status_information