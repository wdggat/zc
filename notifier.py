#!/usr/bin/env python 

import utils

def notify(content):
    utils.execute("python MailSender.py hzliuxiaolong@163.com zucai_2s1 \"%s\"" % str(content))

