Slow ST7789 driver for MicroPython
==================================

This is a slow MicroPython driver for 240x240 ST7789 display without CS pin 
from Ali Express. It also supports 135x240 TTGO Display

Version: 0.2.0

The performance is quite low due to python function call overhead.
If you have a chance to build firmware and you are using 
ESP8266/ESP32 controllers, you should try the fast driver 
https://github.com/devbis/st7789_mpy

Examples
--------

    # ESP8266
    import machine
    import st7789py
    spi = machine.SPI(1, baudrate=40000000, polarity=1)
    display = st7789py.ST7789(spi, 240, 240, reset=machine.Pin(5, machine.Pin.OUT), dc=machine.Pin(4, machine.Pin.OUT))
    display.init()
    display.pixel(120, 120, st7789py.YELLOW)
