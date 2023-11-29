# Python code for Raspberry Pi (Slave)
# Make sure to enable I2C on your Raspberry Pi using raspi-config

import smbus
import time

address = 0x08  # Arduino I2C address

bus = smbus.SMBus(1)  # Raspberry Pi uses SMBus 1

def write_data(data):
    bus.write_i2c_block_data(address, 0, data)
    time.sleep(0.1)  # Allow some time for the Arduino to process

def read_data():
    data = bus.read_i2c_block_data(address, 0, 12)
    return ''.join([chr(byte) for byte in data])

try:
    while True:
        write_data([0])  # Trigger the Arduino to send data
        received_data = read_data()
        print("Received Data: {}".format(received_data))
        time.sleep(1)

except KeyboardInterrupt:
    pass
