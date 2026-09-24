#!/usr/bin/env python3
"""BuggyBot stationary test: camera -> simulated prediction -> LCD.

Run on the Raspberry Pi CM5 after confirming that rpicam-still and the
Waveshare RGB1602 demo work independently. No trained ML model is required.
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

# The Waveshare RGB1602.py module is in the previously tested demo directory.
WAVESHARE_DIR = Path.home() / "LCD1602-RGB-Module-demo" / "Raspberry"
if str(WAVESHARE_DIR) not in sys.path:
    sys.path.insert(0, str(WAVESHARE_DIR))

import RGB1602  # noqa: E402

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

PREDICTIONS = ("STOP", "LEFT", "RIGHT", "SLOW", "SPEED_LIMIT", "NO_ENTRY", "GO", "NONE")
COMMANDS = {
    "STOP": ("STOP SIGN", "STOP", RED),
    "LEFT": ("LEFT TURN", "TURN LEFT", YELLOW),
    "RIGHT": ("RIGHT TURN", "TURN RIGHT", YELLOW),
    "SLOW": ("SLOW DOWN", "REDUCE SPEED", YELLOW),
    "SPEED_LIMIT": ("SPEED LIMIT", "CHECK SPEED", BLUE),
    "NO_ENTRY": ("NO ENTRY", "DO NOT ENTER", RED),
    "GO": ("ROAD CLEAR", "CONTINUE", GREEN),
    "NONE": ("SCANNING...", "NO SIGN DETECTED", WHITE),
}


def display_message(lcd, line1, line2, color):
    """Write two 16-character lines using the tested Waveshare demo API."""
    lcd.clear()
    lcd.setRGB(*color)
    lcd.setCursor(0, 0)
    lcd.printout(line1[:16])
    lcd.setCursor(0, 1)
    lcd.printout(line2[:16])


def capture_image(image_number, image_folder):
    """Take a real picture with the working rpicam-still command."""
    filename = image_folder / f"image_{image_number:04d}.jpg"
    print(f"Capturing: {filename}", flush=True)
    subprocess.run(
        ["rpicam-still", "-n", "-t", "1000", "-o", str(filename)],
        check=True,
    )
    return filename


def simulated_prediction(image_path, mode, prediction_number):
    """Placeholder for the future ML model; does NOT inspect the photo."""
    if mode == "automatic":
        result = PREDICTIONS[prediction_number % len(PREDICTIONS)]
    else:
        print(f"Image captured: {image_path}")
        for number, sign in enumerate(PREDICTIONS, 1):
            print(f"  {number}. {sign}")
        while True:
            choice = input("Choose simulated prediction (1-8): ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(PREDICTIONS):
                result = PREDICTIONS[int(choice) - 1]
                break
            print("Please enter a number from 1 to 8.")
    print(f"SIMULATED prediction (not image recognition): {result}", flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("manual", "automatic"), default="manual")
    parser.add_argument("--interval", type=float, default=5.0,
                        help="Seconds to show each result before the next capture (default: 5)")
    args = parser.parse_args()
    if args.interval < 0:
        parser.error("--interval must be zero or greater")

    image_folder = Path.home() / "buggybot_images"
    image_folder.mkdir(parents=True, exist_ok=True)
    lcd = RGB1602.RGB1602(16, 2)
    try:
        display_message(lcd, "BUGGYBOT", "SYSTEM READY", GREEN)
        time.sleep(2)
        image_number = 1
        prediction_number = 0
        while True:
            display_message(lcd, "CAMERA ACTIVE", "CAPTURING...", BLUE)
            image_path = capture_image(image_number, image_folder)
            prediction = simulated_prediction(image_path, args.mode, prediction_number)
            display_message(lcd, *COMMANDS[prediction])
            print(f"LCD updated: {COMMANDS[prediction][0]} / {COMMANDS[prediction][1]}")
            image_number += 1
            prediction_number += 1
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nStopping BuggyBot.")
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"Camera capture failed: {exc}", file=sys.stderr)
        raise
    finally:
        try:
            display_message(lcd, "BUGGYBOT", "SYSTEM OFF", RED)
            time.sleep(2)
            lcd.clear()
            lcd.setRGB(0, 0, 0)
        except Exception as exc:
            print(f"LCD cleanup issue: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
