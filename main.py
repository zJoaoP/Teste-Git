def sum(a, b):
	return a + b

def sub(a, b):
	return a - b


def div(a, b):
	if b > 0:
		return a / b
	else:
		return 0

def mul(a, b):
	return a * b

def fibonacci(n):
	if n <= 1:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

def fat(n):
	if n > 0:
		return n * fat(n - 1)
	else:
		return 1

if __name__ == '__main__':
	print("Nothing to see here")
