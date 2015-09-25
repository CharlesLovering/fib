import sys

def fib():

	if len(sys.argv) != 2:
		print("Usage: python3 fib_basic.py NUMBER")
		exit(-1);

	n = int(sys.argv[1])
	a = recursive(1, 0, n, 0)
	print(a);


def recursive (a, b, n, i):
	if n == 0:
		return b;
	if n == 1:
		return a;

	a, b = a + b, a;
   
	if n - 2 == i:
		return a;

	else:
		a = recursive(a, b, n, i + 1) 

	return a;

fib();	