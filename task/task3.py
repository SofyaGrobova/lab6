#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    word = input('Введите слово: ')
    lst = []
    for ind, chr in enumerate(word):
        flag = True
        for elem in lst:
            if elem == chr.lower():
                flag = False
                break
        if flag or ind == 0:
            lst.append(chr)

    print(''.join(lst))