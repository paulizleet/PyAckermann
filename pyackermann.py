

import sys

import subprocess

from subprocess import Popen

from subprocess import PIPE



#Change these values to run it on your own machine!

#Path to python command if on windows, or simply 'python' on unix
python_path = "C:\\Users\\pgallagherjr\\Apps\\Python\\python-3.4.4.amd64\\python.exe"  

script_path = "C:\\Users\\pgallagherjr\\ackermann.py"



sys.setrecursionlimit(2500)

limit = sys.getrecursionlimit()


def main(argv):

	if len(argv) != 1:
		
		#Continue recursing on ack where we left off
		
		g = ack(int(argv[1]), int(argv[2]),int(argv[3]))
				
		f=open("ackout",'w')
		f.write(str(g))
		f.close()
		return
		
	print("goin")
	for m in iter(range(0,10)):
		for n in iter(range(0, 10)):
			a=ack(m,n,1)
			
			print("m: " + str(m) + "\tn: " + str(n) + "\ta: " + str(a))


def ack(m, n, d):


	#Python needs some stack frames to actually pull off recursing it past the limit like I want it to.
	#I know that it's less than fifty, so when 
	
	if d < limit - 50:
	
		if m == 0:

			return n + 1
			
		elif m > 0 and n == 0:
			return ack(m-1, 1, d+1)
		
		elif m > 0 and n > 0:

			return ack(m-1, ack(m, n-1, d+1), d+1)
			
	else:
		# We've hit our soft recursion limit on this instance of python.  Time to start another one!
		# Passes the current values of m and n, and resets the depth to 1
		
		#This instance of python will hang on communicate().  When communicate is finished, it means 
		#the called new instance is finished and this one may continue
		Popen([python_path, script_path, str(m), str(n), '1'],stdout=PIPE,	stdin=PIPE, stderr=PIPE).communicate()
		
		# Read the value left behind by instance that just finished and push it up the stack
		f=open("ackout",'r')
		p = f.read().strip()
		
		return int(p)

main(sys.argv)
