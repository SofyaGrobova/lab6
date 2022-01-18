#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    sentnc = input('Введите предложение: ')
    flag = False
    num = 0
    for chr in sentnc:
        if chr.lower() == 'н':
            num += 1
        elif chr == ',':
            flag = True
        if flag:
            break
    print(num)