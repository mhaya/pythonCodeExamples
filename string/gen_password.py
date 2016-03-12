#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import random
import sys

argv = sys.argv

#パスワードで利用可能な文字
base = string.ascii_letters + string.digits+'.)(*&%#@!$'

if len(argv) != 2 :
    print "Password Generator:"
    print "usage: "+sys.argv[0]+" N"
    print "This command generates random N characters from \"" + base + "\""
    sys.exit(0)

n = int(argv[1])

#パスワード文字列を作る
password = ''.join([random.choice(base) for i in range(n)])

print password
