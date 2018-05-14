import smbus

bus = smbus.SMBus(1)
MPU6050_addr = 0x69
# Power management registers
power_mgmt_1 = 0x6b
# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(MPU6050_addr, power_mgmt_1, 0)

def read_raw_word(addr):
    val_h = bus.read_byte_data(MPU6050_addr, addr)
    val_l = bus.read_byte_data(MPU6050_addr, addr+1)
    val = (val_h << 8) + val_l
    return val

def convert_2_2c(data):
    if data >= 0x8000:
        return -((65535 - data) + 1)
    else:
        return data

def scale_gyro_data(data):
    return round(data/131, 2)

def scale_accel_data(data):
    return round(data/16384, 2)
