#!/usr/bin/python3

def lower_alpha_exp():
    for n in range(97, 123):
        if n !=101 and n !=113:
            print('{}'.format(chr(n)), end='')

if __name__ == '__main__':
    lower_alpha_exp()
