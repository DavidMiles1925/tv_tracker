# TV Tracker

## Project Description

This project was developed to help my kids keep track of who's turn in it is to use the television.

## How to use:

# TV Tracker — Raspberry Pi Project

## 🎯 Purpose

This program runs on a Raspberry Pi and is designed to help children take turns using a shared resource (like a TV). Each child has a dedicated button to press when it's their turn. A log is kept of the most recent button press, and the system displays who last took a turn. If a turn hasn't been taken within a specified time window (36 hours), a warning LED is illuminated to alert the household.

---

## 🧑‍🏫 How to Use

### 🟢 Basic Behavior

- Each child has a button wired to a GPIO pin.
- When a button is pressed:

  - The child's name is logged.
  - A message is shown on the 16x2 LCD screen.
  - The corresponding LED is lit to indicate who took the turn.
  - The warning LED (if active) is cleared.

- A **screen toggle button** allows turning the LCD on/off.

- The system checks daily at **7:00 PM**:
  - If no button has been pressed in the last **36 hours**, a **warning LED** is turned on.
  - This warning remains until **any** child presses their button.

### 📟 LCD Display

- Shows the name of the most recent child who took a turn.
- Displays the current time on the second line.
- Automatically updates every second.

### 🔧 Setup

1. Ensure your Pi has Python 3 and `RPi.GPIO` installed.
2. Wire up the following components:
   - Two buttons (for two users)
   - Screen toggle button
   - LCD (16x2) via 4-bit mode
   - Three LEDs: two user indicators + one warning LED
3. Place all scripts in the same directory and set `LOG_DIRECTORY_PATH` appropriately in `config.py`.
4. Run the script using:

```bash
python3 tvtracker.py
```

---

## ⚙️ Developer Notes

### 📁 File Structure

| File           | Purpose                                           |
| -------------- | ------------------------------------------------- |
| `tvtracker.py` | Main program logic and loop                       |
| `logger.py`    | Handles turn logging and console output           |
| `pins.py`      | GPIO setup and control for buttons, LEDs, and LCD |
| `lcd.py`       | Low-level control for a 16x2 HD44780 LCD          |
| `config.py`    | Global constants and settings                     |

### 📌 Important Concepts

- **GPIO Control**: Buttons, relays, and LEDs are managed via the RPi.GPIO library.
- **Logging**: Turn events are written to `lastturn.txt` and a rotating log file in `/home/squirtle/tv_tracker/logs/`.
- **Scheduled Check**: Every day at 7 PM, the system evaluates the time since the last turn and triggers the warning LED if needed.
- **Fail-safe**: The program handles exceptions and cleans up GPIO on shutdown. It can optionally reboot the Pi if an unrecoverable error occurs (`REBOOT_ON_EXCEPTION` in config).

### Setting up the Config File

```bash
sudo nano config.py
```

| Option                           | Possible Values     |   Default Value    | Description                                                                   |
| :------------------------------- | :------------------ | :----------------: | :---------------------------------------------------------------------------- |
| `HOURS_UNTIL_WARNING`            | Any Number          |         36         | The number of hours after a button being pressed before warning light is lit. |
| `SCREEN_ON_BY_DEFAULT`           | True/False          |        True        | Determines whether the screen turns on at system startup.                     |
| `LEDS_ON`                        | True/False          |        True        | This can be used to disable the turn LEDs by setting to `False`               |
| `REBOOT_ON_EXCEPTION`            | True/False          |       False        | Restart if the program encounters an error (NOT RECOMMENDED)                  |
| `CONSOLE_OUTPUT_ON`              | True/False          |        True        | Print statements to the console? (Used for debugging)                         |
| `LOGGING_ENABLED`                | True/False          |        True        | Print activity to logs?                                                       |
| `LOG_DIRECTORY_PATH`             | True/False          |        True        | This is the folder where logs will be stored.                                 |
| `AMELIA_BUTTON_CONSOLE_OUTPUT_1` | 16 Character String |   " BEN'S turn."   | Output for **_Ben's_** Turn (16 Characters including spacesfor LCD screen)    |
| `BEN_BUTTON_CONSOLE_OUTPUT_1`    | 16 Character String | " AMELIA'S turn. " | Output for **_Amelia's_** Turn (16 Characters including spacesfor LCD screen) |

### Example Behavior

**Log:**
[07/29/25 18:53:01]: AMELIA took a turn.

**LCD:**
BEN'S turn.
06:53 PM

---

## Device Construction

### GPIO Information

| Pin Name      | BCM Number | Physical Pin | Description                   |
| :------------ | :--------- | :----------- | :---------------------------- |
| LCD_RS        | 7          | 26           | LCD Register Select           |
| LCD_E         | 8          | 24           | LCD Enable                    |
| LCD_D4        | 25         | 22           | LCD Data Bit 4                |
| LCD_D5        | 24         | 18           | LCD Data Bit 5                |
| LCD_D6        | 23         | 16           | LCD Data Bit 6                |
| LCD_D7        | 18         | 12           | LCD Data Bit 7                |
| CONTROL_PIN   | 17         | 11           | Shared control / warning LED  |
| AMELIA_BUTTON | 26         | 37           | Amelia’s button input         |
| BEN_BUTTON    | 13         | 33           | Ben’s button input            |
| SCREEN_BUTTON | 6          | 31           | Extra screen/button input     |
| LED_BLUE      | 22         | 15           | Blue LED output               |
| LED_PINK      | 27         | 13           | Pink LED output               |
| LED_WARNING   | 17         | 11           | Warning LED (same as control) |

### Wiring Diagram

Diagram Needed

### Gallery

Pictures Needed
