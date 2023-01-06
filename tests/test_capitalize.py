#!/usr/bin/env python3

import sys
sys.path.append('/home/lez/HEXL/capital')
from capital.capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
