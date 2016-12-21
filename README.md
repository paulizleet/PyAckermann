# PyAckermann
Jury rigged '''''multithreaded''''' Ackermann Function algorithm in Python
  
The Ackermann function is a 100% computable function that grows enormously large very very quickly.  At its core it is a very simple algorithm, but because it is recursive - more specifically it calls itself as an argument to calling itself - it is extremely intense to compute for even small values.  [Ackermann Function on Wikipedia](https://en.wikipedia.org/wiki/Ackermann_function)

Python has a hard-ish limit on the depth of recursion with a default of 1000 stack frames.  Hard-ish because you can set the limit to something higher if you want. The Ackermann function needs a lot more than python can handle though, because with too many Python becomes unstable and crashes.	

I thought it would be a fun challenge to get it working in Python	despite that. 

Whenever the function gets too near	the recursion limit, it spawns a new instance of this script that picks up where this one left off!  When it finally reaches the	bottom and starts returning a value, any lower script will write the current value to a file when it reaches the root of its instance before finally terminating.  The instance above that will	read that file and continue passing it up the ladder.


	
