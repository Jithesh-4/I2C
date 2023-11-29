# Python code for Raspberry Pi (Slave)
# Make sure to enable I2C on your Raspberry Pi using raspi-config

import smbus
import time

address = 0x08  # Arduino I2C address
vibration_pin = 17  # GPIO pin where the vibration sensor data is received

bus = smbus.SMBus(1)  # Raspberry Pi uses SMBus 1

def read_data():
    return bus.read_byte(address)

try:
    while True:
        vibration_data = read_data()
        if vibration_data == 1:
            print("Vibration Detected")
        else:
            print("No Vibration")
        time.sleep(1)

except KeyboardInterrupt:
    pass
