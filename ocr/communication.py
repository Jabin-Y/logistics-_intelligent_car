# -*-coding:utf-8-*-
__author__ = 'Code->Y'

import sys
import serial
import time
import platform

def serialinit_move():
    if 'Linux' in platform.platform():
        wheel_com = serial.Serial(
            '/dev/ttyUSB1',
            # '/dev/ttyACM0',
            115200,
            # 9600,
            timeout=2,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE)
        print("连接成功")

    elif 'Windows' in platform.platform():
        wheel_com = serial.Serial(
            'COM60',
            115200,
            timeout=2,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE)

    else:
        raise RuntimeError('Unsupported platform.')

    return wheel_com


def isComplete(serial1):
    while(True):
        e = serial1.readline()
        print("waiting for feedback............",e)
        if b'k' in e:
            print("complete!--------------------------------------")
            return True
        # if b'X' in e:
        # # if b'.OK.\\' in e:
        #     print("led on!")
        #     return True
        # elif b'C' in e:
        #     print("led off!")
        #     return True


def turn_on_led(serial_wheel):
    # pathw = '.a.\\'
    pathw = 'a'
    serial_wheel.write(pathw.encode("utf-8"))
    print("turn led on-----------------------------")
    while(True):
        if isComplete(serial_wheel) == True:
            break


def turn_off_led(serial_wheel):
    # pathw = '.z.\\'
    pathw = 'z'
    serial_wheel.write(pathw.encode("utf-8"))
    print("turn led off----------------------------")
    while(True):
        if isComplete(serial_wheel) == True:
            break

# 识别到文字放下机械臂并吸起货物
def put_down_arm(serial_wheel):
    pathw = 'd'
    serial_wheel.write(pathw.encode('utf-8'))
    print("put down the robotic arm----------------")
    while(True):
        if isComplete(serial_wheel) == True:
            break

# 机器人径直向前行驶
def work_forward_move(serial_wheel):
    pathw = 'fm'
    serial_wheel.write(pathw.encode('utf-8'))
    print("robot forward move----------------")
    while(True):
        if isComplete(serial_wheel) == True:
            break    

# 机器人径直向后退
def work_back_move(serial_wheel):
    pathw = 'bm'
    serial_wheel.write(pathw.encode('utf-8'))
    print("robot back move----------------")
    while(True):
        if isComplete(serial_wheel) == True:
            break

# 机器人向右转
def work_right_move(serial_wheel):
    path = 'rm'
    serial_wheel.write(path.encode('utf-8'))
    print("robot turn right move----------------")
    while(True):
        if isComplete(serial_wheel) == True:
            break 

# 机器人向左转
def work_left_move(serial_wheel):
    path = 'lm'
    serial_wheel.write(path.encode('utf-8'))
    print("robot turn left move----------------")
    while(True):
        if isComplete(serial_wheel) == True:
            break 


# 停止
def work_stop(serial_wheel):
    path = 's'
    serial_wheel.write(path.encode('utf-8'))
    print("stop----------------")
    while(True):
        if isComplete(serial_wheel) == True:
            break 


# 上下层通讯测试程序
if __name__ == "__main__":
    wheel_com = serialinit_move()
    signal = input("开灯y，关灯n:")
    if signal == 'y':
        turn_on_led(wheel_com)
    elif signal == 'n':
        turn_off_led(wheel_com)
    else:
        print("输入错误！")








# import pty
# import os
# import select

# def mkpty():
#     master1, slave = pty.openpty()
#     slaveName1 = os.ttyname(slave)
#     master2, slave = pty.openpty()
#     slaveName2 = os.ttyname(slave)
#     print ('\nslave device names: ', slaveName1, slaveName2)
#     return master1, master2

# if __name__ == "__main__":

#     master1, master2 = mkpty()
#     while True:
#         rl, wl, el = select.select([master1,master2], [], [], 1)
#         for master in rl:
#             data = os.read(master, 128)
#             print ("read %d data." % len(data))
#             if master==master1:
#                 os.write(master2, data)
#             else:
#                 os.write(master1, data)


# import serial
# import binascii
 
# ser = serial.Serial()
 
# def port_open():
#     ser.port = 7            #设置端口号
#     ser.baudrate = 9600     #设置波特率
#     ser.bytesize = 8        #设置数据位
#     ser.stopbits = 1        #设置停止位
#     ser.parity = "N"        #设置校验位
#     ser.open()              #打开串口,要找到对的串口号才会成功
#     if(ser.isOpen()):
#         print("打开成功")
#     else:
#         print("打开失败")
 
# def port_close():
#     ser.close()
#     if (ser.isOpen()):
#         print("关闭失败")
#     else:
#         print("关闭成功")
 
# def send(send_data):
#     if (ser.isOpen()):
#         ser.write(send_data.encode('utf-8'))  #utf-8 编码发送
#         #ser.write(binascii.a2b_hex(send_data))  #Hex发送
#         print("发送成功",send_data)
#     else:
#         print("发送失败")
 
 
# if __name__ == "__main__":
#     port_open()
#     #port_close()
#     while True:
#         send("Hello World!")





