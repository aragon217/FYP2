def main():
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)

    GPIO.output(23, True)
    time.sleep(3)
    GPIO.output(23, False)
    time.sleep(3)
    GPIO.cleanup()
