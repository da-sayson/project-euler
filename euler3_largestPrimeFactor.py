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

	maxPrime=-1
	quotient = n
	while quotient > 1:
		for prime in primes:
			if n % prime == 0:
				print(f"{prime} divides {quotient}")
				if prime > maxPrime:
					maxPrime = prime
				quotient = quotient / prime
	print(f"largest prime is {maxPrime}")

if __name__=="__main__":
	main()