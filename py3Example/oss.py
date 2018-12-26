# -*- coding: utf-8 -*-
# Created by bida on 2018/12/12
import socket
import subprocess
import os
import signal

# kill process
# LINUX
proc = subprocess.Popen(['pgrep', 'java', 'python'], stdout=subprocess.PIPE)
for pid in proc.stdout:
    print(int(pid))
    os.kill(int(pid), signal.SIGTERM)
#
#
# # Windows
# os.system('taskkill /im notepad.exe')
# os.system('tskill ping')


# # get IP address
# # Mac, Windows
# import socket
# socket.gethostbyname(socket.gethostname())
# #ALL
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(('8.8.8.8', 80))
# s.getsockname()[0]