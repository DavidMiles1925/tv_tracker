import RPi.GPIO as GPIO
from logger import console_and_log, log_last_turn, get_last_turn
from lcd import LCD_LINE_1, LCD_LINE_2, lcd_text, lcd_init
from pins import AMELIA_BUTTON, BEN_BUTTON, SCREEN_BUTTON, LED_WARNING, toggle_led, setup_pins, toggle_relay
from config import AMELIA_BUTTON_CONSOLE_OUTPUT_1, BEN_BUTTON_CONSOLE_OUTPUT_1, REBOOT_ON_EXCEPTION, HOURS_UNTIL_WARNING
from time import sleep
from datetime import datetime
from datetime import time as dt_time
import os

warning_checked_today = False

def cleanup():
    lcd_init()
    GPIO.cleanup()

def check_last_turn_for_warning():
    child, last_time = get_last_turn()
    now = datetime.now()
    if last_time is not None:
        hours_since = (now - last_time).total_seconds() / 3600
    else:
        hours_since = 0

    if hours_since > HOURS_UNTIL_WARNING:
        GPIO.output(LED_WARNING, GPIO.HIGH)
    else:
        GPIO.output(LED_WARNING, GPIO.LOW)


def check_button(pin, message1="", child="NONE"):
    # Check if child's name should display.
    if GPIO.input(pin) ==  False:
        console_and_log(f"{child} took a turn.")
        log_last_turn(child)
        lcd_text(message1, LCD_LINE_1)

        toggle_led(child)

        sleep(2)


def check_screen_button(pin):
    if GPIO.input(pin) ==  False:
        toggle_relay()
        show_last_turn()


def display_the_time():
    the_time = datetime.now().strftime("%I:%M %p")
    time_string = f"    {the_time}    "

    lcd_text(time_string, LCD_LINE_2)


def show_last_turn():
    child = get_last_turn()
    toggle_led(child)
    #sleep(0.1)
    lcd_init()
    sleep(0.1)
    if child == "NO_FILE":
        lcd_text(" No File Found. ", LCD_LINE_1)
    elif child == "AMELIA":
        lcd_text(AMELIA_BUTTON_CONSOLE_OUTPUT_1, LCD_LINE_1)
    elif child == "BEN":
        lcd_text(BEN_BUTTON_CONSOLE_OUTPUT_1, LCD_LINE_1)
    else:
        lcd_text("FILE READ ERROR ", LCD_LINE_1)
        console_and_log("There was a problem reading the file. It exists, but it can't find a name.")


if __name__ == "__main__":
    try:
        setup_pins()

        lcd_init()

        console_and_log("Program Started")

        child, last_time = get_last_turn()
        
        console_and_log(f"{child} had the last turn.")

        # lcd_text("Program Started", LCD_LINE_1)
        show_last_turn()

        while True:
            display_the_time()

            now = datetime.now()
            if now.time() >= dt_time(19, 0) and not warning_checked_today:
                check_last_turn_for_warning()
                warning_checked_today = True
            elif now.time() < dt_time(19, 0):
                warning_checked_today = False

            check_button(AMELIA_BUTTON, AMELIA_BUTTON_CONSOLE_OUTPUT_1, "AMELIA")

            check_button(BEN_BUTTON, BEN_BUTTON_CONSOLE_OUTPUT_1, "BEN")

            check_screen_button(SCREEN_BUTTON)

    except KeyboardInterrupt:
        console_and_log("CTRL-C PRESSED")

    except Exception as e:
        console_and_log(f"ERROR: {e.args}  {e}")
        if REBOOT_ON_EXCEPTION:
            sleep(20)
            console_and_log("SYSTEM REBOOTED")
            os.system("sudo reboot")

    finally:
        console_and_log("PROGRAM CLOSED")
        cleanup()
