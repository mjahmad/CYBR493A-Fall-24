#!/usr/bin/env python3
# ASCII generator
# Uses chr() to create ASCII characters
# By Ed Goad
# 2/27/2021

for i in range(127):
    if i >=65 and i <=90:
        print("{0}\t'{1}'".format(i,chr(i).lower()))
    elif i >=97 and i <=122:
        print("{0}\t'{1}'".format(i,chr(i).upper()))
