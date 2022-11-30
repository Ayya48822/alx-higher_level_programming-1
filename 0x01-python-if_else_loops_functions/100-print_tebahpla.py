#!/usr/bin/python3

alphabet = ""
for i in reversed(range(97, 123)):
    if i % 2 == 0:
        alphabet = chr(i)
    else:
        alphabet = chr(i - 32)
    print("{}".format(alphabet), end="")
