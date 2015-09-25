import sys

if len(sys.argv) != 2:
	print("Usage: python3 fib_basic.py NUMBER")
	exit(-1);

n = int(sys.argv[1])

a = 1
b = 0

if n == 0:
    print(b);
    exit(0);
if n == 1:
	print(a);
	exit(0);

i = 0;
while ((n - 1) > i):
    a, b = a + b, a;
    i += 1;

print(a);
exit(0);
