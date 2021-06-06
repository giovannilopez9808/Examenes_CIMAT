import math
import sys


def is_two_power(number):
    if math.log2(number) % 1 == 0:
        print("true")
    else:
        print("false")


is_two_power(float(sys.argv[1]))
