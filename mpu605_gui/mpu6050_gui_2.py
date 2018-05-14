from tkinter import *
from my_GUI import GUI
from my_mpu6050_lib import *
import time
import threading

def thread_update_gui():
    '''
    Thread to update the GUI
    '''
    while True:
        """ update gyroscope data """
        x = read_raw_word(0x43)
        y = read_raw_word(0x45)
        z = read_raw_word(0x47)
        gyro_raw.setxyz(x, y, z)

        x_c = convert_2_2c(x)
        y_c = convert_2_2c(y)
        z_c = convert_2_2c(z)
        gyro_2c.setxyz(x_c, y_c, z_c)

        x_s = scale_gyro_data(x_c)
        y_s = scale_gyro_data(y_c)
        z_s = scale_gyro_data(z_c)
        gyro_scale.setxyz(x_s, y_s, z_s)

        """ update accelerometer data """
        x = read_raw_word(0x3B)
        y = read_raw_word(0x3D)
        z = read_raw_word(0x3F)
        accel_raw.setxyz(x, y, z)

        x_c = convert_2_2c(x)
        y_c = convert_2_2c(y)
        z_c = convert_2_2c(z)
        accel_2c.setxyz(x_c, y_c, z_c)

        x_s = scale_accel_data(x_c)
        y_s = scale_accel_data(y_c)
        z_s = scale_accel_data(z_c)
        accel_scale.setxyz(x_s, y_s, z_s)

        time.sleep(.3)

win = Tk()
win.title("MPU6050")

"""
    Gyroscope related code
"""

""" Gyroscope Heading """
lbl_gyro_heading = Label(win, text="GYROSCOPE")
lbl_gyro_heading.grid(columnspan=5, row =0)

''' Gyro 1st column '''
gyro_1st_column=GUI()
gyro_fram = gyro_1st_column.createGUI(win)
gyro_fram.grid(row=1 , column=1)
gyro_1st_column.setxyz("X", "Y", "Z")
gyro_1st_column.setColHeading("------")
gyro_1st_column.changeFgColor("black")

""" Gyro 2nd column for raw data """
gyro_raw=GUI()
gyro_raw.createGUI(win).grid(row=1, column=2)
gyro_raw.setColHeading("Raw Data")
gyro_raw.changeFgColor("Green")

""" Gyro 3rd column for 2's complement data """
gyro_2c=GUI()
gyro_2c.createGUI(win).grid(row=1, column=3)
gyro_2c.setColHeading("2's comp")
gyro_2c.changeFgColor("Green")

""" Gyro 4th column for scaled data """
gyro_scale=GUI()
gyro_scale.createGUI(win).grid(row=1, column=4)
gyro_scale.setColHeading("Scaled Data")
gyro_scale.changeFgColor("Green")

""" Gyro 5th column for --- data """
gyro_=GUI()
gyro_.createGUI(win).grid(row=1, column=5)
gyro_.setxyz(1,2,3)
gyro_.setColHeading("---- Data")
gyro_.changeFgColor("Green")

"""
    Acceleromter related code
"""

""" Accelerometer Heading """
lbl_gyro_heading = Label(win, text="ACCELEROMETER")
lbl_gyro_heading.grid(columnspan=5, row =2)

''' Accel 1st column '''
accel_1st_column=GUI()
accel_fram = accel_1st_column.createGUI(win)
accel_fram.grid(row=3 , column=1)
accel_1st_column.setxyz("X", "Y", "Z")
accel_1st_column.setColHeading("------")
accel_1st_column.changeFgColor("black")

""" Accel 2nd column for raw data """
accel_raw=GUI()
accel_raw.createGUI(win).grid(row=3, column=2)
accel_raw.setColHeading("Raw Data")
accel_raw.changeFgColor("Green")

""" Accel 3rd column for 2's complement data """
accel_2c=GUI()
accel_2c.createGUI(win).grid(row=3, column=3)
accel_2c.setColHeading("2's comp")
accel_2c.changeFgColor("Green")

""" Accel 4th column for scaled data """
accel_scale=GUI()
accel_scale.createGUI(win).grid(row=3, column=4)
accel_scale.setColHeading("Scaled Data")
accel_scale.changeFgColor("Green")

""" Accel 5th column for ---- data """
accel_=GUI()
accel_.createGUI(win).grid(row=3, column=5)
accel_.setColHeading("---- Data")
accel_.changeFgColor("Green")

# Create the thread for updating GUI
th1=threading.Thread(target=thread_update_gui)
# start the thread
th1.start()

win.mainloop()
