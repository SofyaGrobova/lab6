#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    lst = []
    sentnc = input('Введите предложение: ')
    for chr in sentnc:
        if chr.lower() == 'и':
            print(chr)
