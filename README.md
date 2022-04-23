# mcp4922-py
MicroPython library for the MCP4922 12 Bit DAC

## Basic usage

```py
from mcp4922 import MCP4922

dac = MCP4922()
dac.write_value(2000) # Value between 0 and 4096
```
This usage requires the MCP4922 to be wired in the following way:

Pin 0 to pin 5 on the MCP4922 (SDI)

Pin 1 to pin 4 on the MCP4922 (SCK)

Pin 2 to pin 3 on the MCP4922 (CS)

<img width="484" alt="image" src="https://user-images.githubusercontent.com/27863547/164908850-3debe29f-17bc-43ed-a5fb-6b8f369f6b01.png">


## Using different pin numbers
```py
dac = MCP4922(mosi_pin=0, sck_pin=1, cs_pin=2)
```

## Output options

Take a look at the datasheet for more information about these options.

```py
from mcp4922 import MCP4922, OUTPUT_B, UNBUFFERED, GAIN_2X, SHUTDOWN

dac.write_value(2000, output_dac=OUTPUT_B) # Using output B instead of A
dac.write_value(2000, buffer_mode=UNBUFFERED) # Don't use a buffer for the output
dac.write_value(2000, gain_mode=GAIN_2X) # Output gain of 2
dac.write_value(2000, output_mode=SHUTDOWN) # Disable one of the outputs
```
