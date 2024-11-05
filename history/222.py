#舵机
from math import e  # noqa: F401
import re  # noqa: F401
from time import sleep
import serial 
from serial.serialutil import SerialException
from pymodbus.client.serial import ModbusSerialClient as ModbusClient

# 初始化全局变量
result = [2, 2]
n = 0
door = 0

# 初始化电机连接,函数在连接成功时函数值为1，否则为0
def serlink():
    global ser
    try:
        ser = serial.Serial('COM1', 115200, timeout=1)
        return 1
    except SerialException:
        print("Serial port link not found")
        return 0

# 发送指令
def send_command(hex_data):
    try:
        serlink()
        sleep(0.1)
        ser.write(bytes.fromhex(hex_data))
        print("Command sent")
        ser.close()
        sleep(0.1)
    except SerialException as err:
        print(f"An error occurred: {err}")
        ser.close()
        ser.open()

# 读取指定地址的保持寄存器
def read_holding_registers(address, count, unit):
    try:
        result = client.read_holding_registers(address, count, slave=unit)
        if result.isError():
            print(f"An error occurred: {result}")
        else:
            return result.registers
    except Exception as err:
        print(f"An exception occurred: {err}")
        return None

# 设置门的状态
def setup():
    global door
    if result[0] == 1:  # check if there is a hand
        if result[1] == 0 and n == 1:  # check if the hand is open:  # check if there is a door:  # open door
            send_command('01 06 00 80 03 84 88 B1')
            #shutlight()
            print("Door is opening")
        elif result[1] == 1 and n == 0:  # close door 
            send_command('01 06 00 80 01 2C 88 6F')
            #shutlight()
            print("Door is closing")
        else:
            if n == 1 or n == 0:
                print("Door is already in the desired position")
                print(f"n = {n}, door = {door}")
            else:
                print("Invalid setup input")
    else: 
        print("\r Please remove the hand before setting up the door", end=" ")
        ser.close()

# 键盘输入n值
def input_n():
    global n
    try:
        n = int(input("Enter 1 to open the door or 0 to close the door: "))
    except ValueError:
        print("Invalid input")

# 点亮手电筒
def lightup():
    while result[0] == 1:  # check if there is a hand
        print("\rputting hand into it",end=" ")
        sleep(1)
        readmodbus()
    send_command('02 06 00 00 00 01 48 39')  # 手来开
    readmodbus()

#  条件关闭手电筒
def cklightdown():
    if result[0] == 1:  # check if there is a hand  
        send_command('02 06 00 00 00 00 89 F9')  # 手去关

# 强制关闭手电筒
def shutlight():
    send_command('02 06 00 00 00 00 89 F9')

# 读取modbus数据
def readmodbus():
    global result
    # 连接到串口
    client.connect()

    D = read_holding_registers(0x101, 1, 1)  # (address, count, unit)
    if D:
        p = round(D[0], -2)
        if p == 900:
            print("The door is open")
            door = 1
        elif p == 300:
            print("\rThe door is closed",end=" ")
            door = 0
        else:
            print("The door is in an unknown position")
            door = None
    else:
        print("Failed to read registers")

    hand = read_holding_registers(0x200, 1, 2)  # (address, count, unit)
    if hand:
        if hand[0] == 1:
            print("\rthere is no hand{}".format(hand[0]), end=" ")
        else:
            print("\rthere is a hand",end=" ")
    else:
        print("Failed to read registers")
    
    # 把读到的参数存入列表，按【手、门】的顺序
    result = []
    if hand and door is not None:
        result.append(hand[0])
        result.append(door)
        
    # 关闭串口连接，检测完毕
    client.close()
    return 1



# 配置串口参数
client = ModbusClient(port='COM1', baudrate=115200, timeout=1)

# 主循环
while True:
    if serlink()==1:        # 循环 检测串口连接
        print("\nSerial port found", end="")        
        ser.close()
        
        readmodbus()        
        lightup()
        input_n()
        readmodbus()
        sleep(0.5)
        setup()
        sleep(2)
        readmodbus()
        n=0
        setup()
        shutlight()
        ser.close()
    else:
        print("\rSerial port not found", end=" ")
        sleep(1)
        continue