from machine import Pin, SoftSPI

OUTPUT_A, OUTPUT_B = 0, 1
GAIN_1X, GAIN_2X = 1, 0 
BUFFERED, UNBUFFERED = 1, 0
OUTPUT_ACTIVE, OUTPUT_SHUTDOWN = 1, 0

class MCP4922:
    def __init__(self, mosi_pin=0, sck_pin=1, cs_pin=2, baudrate=100000):
        self.spi = SoftSPI(baudrate=baudrate, polarity=1, phase=0, mosi=Pin(mosi_pin), sck=Pin(sck_pin), miso=Pin(29))
        self.cs = Pin(cs_pin, mode=Pin.OUT)

    def write_value(self, value, output_dac=OUTPUT_A, buffer_mode=BUFFERED, gain_mode=GAIN_1X, output_mode=OUTPUT_ACTIVE):
        configBits = output_dac << 3 | buffer_mode << 2 | gain_mode << 1 | output_mode
        first_four_bits = value & 0XF00
        last_eight_bits = value & 0xFF
        try:
            self.cs.value(0)
            self.spi.write(bytearray([configBits << 4 | first_four_bits >> 8 ]))
            self.spi.write(bytearray([last_eight_bits]))
        finally:
            self.cs.value(1) 
