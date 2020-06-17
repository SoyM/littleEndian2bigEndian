#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import


def transToMyHex(data):
    __str_tmp = hex(data)[2:]
    if len(__str_tmp) == 1:
        return '0'+__str_tmp
    else:
        return __str_tmp


if __name__ == "__main__":

    bin_file = "/home/soym/Desktop/test_little.bin"
    f = open(bin_file, "rb")
    data = f.read()
    print(len(data))
    if len(data) % 4 == 0:
        print("%4 ok")
    tmp = []
    data_trans = ''
    for i in range(len(data)):
        if (i+1) % 4 == 0:
            print(transToMyHex(data[i]))
            data_trans += transToMyHex(data[i])
            data_trans += transToMyHex(data[i-1])
            data_trans += transToMyHex(data[i-2])
            data_trans += transToMyHex(data[i-3])
            # data_trans = data_trans + chr(data[i])+chr(data[i-1]) + chr(data[i-2])+chr(data[i-3])
    print(data_trans)

    bin_file_trans = "/home/soym/Desktop/test_bigEndian.bin"
    with open(bin_file_trans, 'wb') as file_object:
        file_object.write(bytes.fromhex(data_trans))
