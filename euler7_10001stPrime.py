from math import ceil, sqrt

def main():
	n = 600851475143

	# finds primes
	sieve = [True]*ceil(sqrt(n))
	sieve[0] = False
	sieve[1] = False
	for idx in range(2,ceil(sqrt(n))):
		for multiplier in range(2, ceil(sqrt(n)/2)):
			if idx * multiplier >= len(sieve):
				break
			sieve[idx*multiplier] = False

	primes = []
	for idx, isPrime in enumerate(sieve):
		if isPrime:
			primes.append(idx)

	print(primes[10000])

if __name__=="__main__":
	main()