from traceback import print_tb

try:
    print(1/0)
except ZeroDivisionError:
    print('sorry, try another arithmetic format!')
