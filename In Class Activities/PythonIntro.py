"""
Python Introduction
9/12/2024
Author : MJ Ahmad
"""


def printVarInfo():
    """
    This simple function prints out the types of two local variables
    :return: N/A
    """
    # A variable to store an integer
    x = 5
    print(type(x))
    y = 3.1
    print(type(y))


def methodThatAcceptsData(x, y, z):
    """
    This method accepts three variables and prints out their data types
    :param x: First variable
    :param y: Second Variable
    :param z: Third Variable
    :return: /N/A
    """
    print("x is ", type(x))
    print("y is ", type(y))
    print("z is ", type(z))


methodThatAcceptsData(100, [0, 1, 2, 3, 4, 5], 'WVU')
# printVarInfo()

#
#
# ips = ['192.168.10.1', 10, '192.168.10.3', '192.168.10.4']
# print(type(ips))
# print(type(ips[1]))
# print(ips[0] + ips[3])
# print(ips)
# for cat in ips:
#     print(cat)
#
# if ips[1] >= 20:
#     print('The value is indeed greater than 20')
# else:
#     print('The value is NOT greater than 20')
#
# name = "MJ Ahmad"
# print(type(name))
#
# yourName = 'Sarah Conor'
# print(type(yourName))
