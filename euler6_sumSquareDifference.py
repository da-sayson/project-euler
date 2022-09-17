def main():
	LOWEST_NATURAL_NUMBER = 1
	HIGHEST_NATURAL_NUMBER = 100
	sumOfSquares = sum(v*v for v in range(LOWEST_NATURAL_NUMBER, HIGHEST_NATURAL_NUMBER+1))
	squareOfSum = sum(range(LOWEST_NATURAL_NUMBER, HIGHEST_NATURAL_NUMBER+1))**2
	print(abs(sumOfSquares-squareOfSum))

if __name__=="__main__":
	main()