import sys
sys.set_int_max_str_digits(0)
while True:
    b = int(input("写一个数字:/Enter a number: "))
    a = int(input("再次写一个数字:/Enter a number again: "))
    if a == 0:
        print(0)
    elif a > 0:
        print(b**a)
        