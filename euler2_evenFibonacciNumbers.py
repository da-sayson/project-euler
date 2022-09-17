def main():
	sumOfEven = 0
	fib1 = 1
	fib2 = 2
	while fib2 < 4000000:
		if fib2 % 2 == 0:
			sumOfEven += fib2
		fib3 = fib1 + fib2
		fib1 = fib2
		fib2 = fib3
	print(sumOfEven)

if __name__=="__main__":
	main()