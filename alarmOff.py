def main():
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)

    GPIO.output(23, False)
    time.sleep(5)
    GPIO.cleanup()
