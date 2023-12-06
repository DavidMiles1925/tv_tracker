import RPi.GPIO as GPIO
from logger import console_and_log, log_last_turn, get_last_turn
from lcd import LCD_LINE_1, LCD_LINE_2, lcd_text, lcd_init
from pins import AMELIA_BUTTON, BEN_BUTTON, SCREEN_BUTTON, toggle_led, setup_pins, toggle_relay
from config import AMELIA_BUTTON_CONSOLE_OUTPUT_1, AMELIA_BUTTON_CONSOLE_OUTPUT_2, BEN_BUTTON_CONSOLE_OUTPUT_1, BEN_BUTTON_CONSOLE_OUTPUT_2, REBOOT_ON_EXCEPTION
from time import sleep
import os


def cleanup():
    lcd_init()
    GPIO.cleanup()


def check_button(pin, message1="", message2="", child="NONE"):
    if GPIO.input(pin) ==  False:
        console_and_log(f"{child} took a turn.")
        log_last_turn(child)
        lcd_text(message1, LCD_LINE_1)
        lcd_text(message2, LCD_LINE_2)

        toggle_led(child)

        sleep(2)


def check_screen_button(pin):
    if GPIO.input(pin) ==  False:
        toggle_relay()
        show_last_turn()


def show_last_turn():
    child = get_last_turn()
    toggle_led(child)
    #sleep(0.1)
    lcd_init()
    sleep(0.1)
    if child == " No File Found. ":
        lcd_text(" No File Found. ", LCD_LINE_1)
    elif child == "BEN":
        lcd_text(AMELIA_BUTTON_CONSOLE_OUTPUT_1, LCD_LINE_1)
        lcd_text(AMELIA_BUTTON_CONSOLE_OUTPUT_2, LCD_LINE_2)
    elif child == "AMELIA":
        lcd_text(BEN_BUTTON_CONSOLE_OUTPUT_1, LCD_LINE_1)
        lcd_text(BEN_BUTTON_CONSOLE_OUTPUT_2, LCD_LINE_2)
    else:
        lcd_text(" Error: Input   ", LCD_LINE_1)
        lcd_text(" did not match. ", LCD_LINE_2)
    # lcd_text(f"{child} had the", LCD_LINE_1)
    # if child != " No File Found. ":
    #     lcd_text("last turn.", LCD_LINE_2)


if __name__ == "__main__":
    try:
        setup_pins()

        lcd_init()

        console_and_log("Program Started")
        console_and_log(f"{get_last_turn()} had the last turn.")

        # lcd_text("Program Started", LCD_LINE_1)
        show_last_turn()

        while True:
            check_button(AMELIA_BUTTON, AMELIA_BUTTON_CONSOLE_OUTPUT_1, AMELIA_BUTTON_CONSOLE_OUTPUT_2, "AMELIA")

            check_button(BEN_BUTTON, BEN_BUTTON_CONSOLE_OUTPUT_1, BEN_BUTTON_CONSOLE_OUTPUT_2, "BEN")

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
