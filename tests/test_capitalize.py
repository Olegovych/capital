#!/usr/bin/env python3

import sys
sys.path.append('/home/lez/HEXL/capital')
from capital.capitalize import capitalize

assert capitalize('hello') == 'Hello'

assert capitalize('') == ''

print('Все тесты пройдены!')
