import numpy as np
import sys

# based off Matrix Equation Property of Fib
# does not seem to work for values over 92 because it maxes out for some reason
# getting negative numbers - I think numpy array values can't go over some relatively low val
# compared to normal - overflow issues

if (len(sys.argv) != 2):
	print("python fib_matrix.py NUMBER");
	exit(-1);
else:
	n = int(sys.argv[1])

if n == 0:
	print(0);
	exit(0);

base = np.array(((1,1), (1, 0)) )
result = np.array(((1,1), (1, 0)) )

for x in xrange(0, n - 1):
	result = np.dot(result, base);
	val = result[1][0]
	print(val);

val = result[1][0]
print(val);
print(result);
