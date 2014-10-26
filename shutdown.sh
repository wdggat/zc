#!/usr/bin/bash 

kill -9 `ps aux | grep 'python executor.py' | awk '{print $2}'`
