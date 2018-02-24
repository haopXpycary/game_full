#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
RUNME.py --Anything Begin It.
'''
__author__ = "haopXpycary"
__email__  = "haopxpycary@foxmail.com"
__QQ__     = "2641725961"

from loveProtect import *
from os import uname,chdir

chdir(__file__[:__file__.rfind("/")])
if uname()[0] != "Linux":
    print("暂不支持window系列")
    exit(1)
from __init__ import *