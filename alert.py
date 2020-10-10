#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os


def sendmessage():
     return os.system('notify-send', "this ")
sendmessage()