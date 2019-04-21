# code for micropython 1.10 on esp8266

import random

import machine
import st7789py as st7789
import time


def main():
    spi = machine.SPI(1, baudrate=40000000, polarity=1)
    display = st7789.ST7789(
        spi, 240, 240,
        reset=machine.Pin(5, machine.Pin.OUT),
        dc=machine.Pin(2, machine.Pin.OUT),
    )
    display.init()

    while True:
        display.fill(
            st7789.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8),
            ),
        )
        # Pause 2 seconds.
        time.sleep(2)
