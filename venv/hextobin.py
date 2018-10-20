import binascii
import struct
def example(express, result=None):
    if result == None:
        result = eval(express)
    print(result)


if __name__ == '__main__':
    #print("16进制转10进制", end=': ')
    a=input()
    example("int('b', 16)")
