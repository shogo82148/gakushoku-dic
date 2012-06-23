#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pyimedic
import pyimedic.googleime
import pyimedic.msime
import pyimedic.dctx

with open('gakushoku-dic.txt') as f:
    d = pyimedic.googleime.read(f)

with open('gakushoku-dic-msime.txt', 'w') as f:
    pyimedic.msime.write(f, d)

with open('gakushoku-dic.dctx', 'w') as f:
    pyimedic.dctx.write(f,d)
