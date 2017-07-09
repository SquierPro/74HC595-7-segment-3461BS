import time
from pyA20.gpio import gpio
from pyA20.gpio import connector
from pyA20.gpio import port

dio = connector.gpio1p13
rclk = connector.gpio1p11
sclk = connector.gpio1p12


digit = [ 
      "11000000",# 0
      "11111001",# 1
      "10100100",# 2
      "10110000",# 3
      "10011001",# 4
      "10010010",# 5
      "10000010",# 6
      "11111000",# 7
      "10000000",# 8
      "10010000",# 9 
      "11111111",# 10 Clear
      "10011100",# 11 Gradus
      "10001000",# 12 A
      "10000011",# 13 b
      "11000110",# 14 C
      "10100001",# 15 d
      "10000110",# 16 E
      "10001110",# 17 F
      "11000011",# 18 G
      "10001001",# 19 H
      "11111001",# 20 I
      "11000111",# 21 L
      "10101011",# 22 n
      "11000000",# 23 O
      "10001100",# 24 P
      "10011000",# 25 q
      "10101111",# 26 r
      "10010010",# 27 S
      "10000111",# 28 t
      "11000001",# 29 U
      "10010001",# 30 Y
      "10111111",# 31 -
];


gpio.init()
gpio.setcfg(dio, gpio.OUTPUT)
gpio.setcfg(rclk, gpio.OUTPUT)
gpio.setcfg(sclk, gpio.OUTPUT)

gpio.output(dio, 0)
gpio.output(rclk, 0)
gpio.output(sclk, 0)


def hc595(data, num):
    for i in range(0, 8):
        gpio.output(dio, int(data[i]))
        gpio.output(sclk, 1)
        #time.sleep(0.001)
        gpio.output(sclk, 0)

    for i in range(0, 8):
        if num==7-i:
            gpio.output(dio, 1)
        else:
            gpio.output(dio, 0)
        gpio.output(sclk, 1)
        #time.sleep(0.001)
        gpio.output(sclk, 0)
    
    hc595_out()

def hc595_out():
    gpio.output(rclk, 1)
    time.sleep(0.001)
    gpio.output(rclk, 0)

val=[10,10,10,10]
i=10000
while True:
    i+=1
    arr=list(str(i/10))
    
    hc595(digit[int(arr[0])],3)
    hc595(digit[int(arr[1])],2)
    hc595(digit[int(arr[2])],1)
    hc595(digit[int(arr[3])],0)


