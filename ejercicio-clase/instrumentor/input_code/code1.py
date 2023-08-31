import time

def foo():
    bar(2,3)
    time.sleep(3)

def bar(a,b):
    time.sleep(5)

def main():
    foo()


main()