##############################
##############################
#####                    #####
#####  RUNTIME OPTIONS   #####
#####                    #####
##############################
##############################

HOURS_UNTIL_WARNING = 36

SCREEN_ON_BY_DEFAULT = True

LEDS_ON = True

REBOOT_ON_EXCEPTION = False


##############################
##############################
#####                    #####
#####      LOGGING       #####
#####                    #####
##############################
##############################


CONSOLE_OUTPUT_ON = True

LOGGING_ENABLED = True

LOG_DIRECTORY_PATH = "/home/squirtle/tv_tracker/logs/"


##############################
##############################
#####                    #####
#####  OUTPUT CONSTNATS  #####
#####                    #####
##############################
##############################

                               #  1234567890123456
AMELIA_BUTTON_CONSOLE_OUTPUT_1 = "   BEN'S turn.  "

                            #  1234567890123456
BEN_BUTTON_CONSOLE_OUTPUT_1 = " AMELIA'S turn. "


##############################
##############################
#####                    #####
#####     PULL FILES     #####
#####                    #####
##############################
##############################

REMOTE_HOST = "192.168.1.177"
PI_USERNAME = "squirtle"
WIN_USERNAME = "David"

REMOTE_PATH_PHOTO = None
REMOTE_PATH_VIDEO = f"/home/{PI_USERNAME}/tv_tracker/logs/"
LOCAL_PATH = f"C:/Users/{WIN_USERNAME}/Downloads"