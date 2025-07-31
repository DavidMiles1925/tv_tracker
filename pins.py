import RPi.GPIO as GPIO
from config import LEDS_ON, SCREEN_ON_BY_DEFAULT
from time import sleep
from lcd import lcd_init


LCD_RS = 7 
LCD_E  = 8 
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18

CONTROL_PIN = 17
screen_is_on = SCREEN_ON_BY_DEFAULT

AMELIA_BUTTON = 26
BEN_BUTTON  = 13
SCREEN_BUTTON = 6

LED_BLUE = 22
LED_PINK = 27

LED_WARNING = 12


def pin_out(pin, status=True):
    if status:
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)
    

def setmode():
    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)


def setup_lcd_pins():
    lcd_array = [LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7]

    for item in lcd_array:
        GPIO.setup(item, GPIO.OUT)
        pin_out(item, False)


def setup_relay_pins():

    GPIO.setup(CONTROL_PIN, GPIO.OUT)
    pin_out(CONTROL_PIN, SCREEN_ON_BY_DEFAULT)
    sleep(0.1)
    lcd_init()


def toggle_relay():
    global screen_is_on

    if screen_is_on == True:
        GPIO.output(CONTROL_PIN, GPIO.LOW)
    else:
        GPIO.output(CONTROL_PIN, GPIO.HIGH)

    screen_is_on = not screen_is_on
    sleep(0.2)


def setup_button_pins():

    button_array = [AMELIA_BUTTON, BEN_BUTTON, SCREEN_BUTTON]

    for item in button_array:
        GPIO.setup(item, GPIO.IN)


def setup_led_pins():
    led_array = [LED_BLUE, LED_PINK, LED_WARNING]

    for item in led_array:
        GPIO.setup(item, GPIO.OUT)
        pin_out(item, False)


def setup_pins():
    setmode()
    setup_lcd_pins()
    setup_relay_pins()
    setup_button_pins()
    setup_led_pins()


def toggle_led(child):
    if LEDS_ON:
        if child == "AMELIA":
            pin_out(LED_BLUE, True)
            pin_out(LED_PINK, False)
        elif child == "BEN":
            pin_out(LED_BLUE, False)
            pin_out(LED_PINK, True)
        else:
            pin_out(LED_BLUE, False)
            pin_out(LED_PINK, False)