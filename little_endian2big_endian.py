#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Little_endian to big_endian.')
parser.add_argument(
    'binFile',  default="./test_little.bin", help='binary file')
parser.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument(
    '--output',  default="./test_bigEndian.bin", help='output big_endian bin file')
parser.add_argument('--bitSize', type=int, default=32,
                    help='architecture bit size,support:8,16,32,64')

args = parser.parse_args()


def transToMyHex(data):
    __str_tmp = hex(data)[2:]
    if len(__str_tmp) == 1:
        return '0'+__str_tmp
    else:
        return __str_tmp


if __name__ == "__main__":
    f = open(args.binFile, "rb")
    data = f.read()
    print("len: {}".format(len(data)))

    tmp_size = int(int(args.bitSize)/8)
    if len(data) % tmp_size == 0:
        print("split_size: {}".format(int(tmp_size)))

        tmp = []
        data_trans = ''
        for i in range(len(data)):
            if (i+1) % tmp_size == 0:
                data_trans += transToMyHex(data[i])
                data_trans += transToMyHex(data[i-1])
                data_trans += transToMyHex(data[i-2])
                data_trans += transToMyHex(data[i-3])
        if args.verbose:
            print(data_trans)

        with open(args.output, 'wb') as file_object:
            file_object.write(bytes.fromhex(data_trans))

        print("Trans success\nOutput file: {}".format(args.output))
