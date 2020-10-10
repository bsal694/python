#!/usr/bin/env python3
import re
import sys
import os
import subprocess
worktime=subprocess.run(['uptime'],capture_output=True)
sample=worktime.stdout.decode()
pattern=r" (\d{,2} )"
text=re.search(pattern,sample)
a=int(text.group())


if a>20:
	




	os.system('spd-say --rate=10  "Now the pc will 	shutdown ................"')

	os.system("shutdown now -h")