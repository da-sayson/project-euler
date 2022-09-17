def isPalindrome(n):
	reverse = int(str(n)[::-1])
	return n==reverse

def main():
	largestPalindrome=None
	LARGEST_3_DIGIT_NUMBER = 999
	RANGE_RESTRICTION = 799
	for left in range(LARGEST_3_DIGIT_NUMBER,RANGE_RESTRICTION,-1):
		for right in range(LARGEST_3_DIGIT_NUMBER,RANGE_RESTRICTION,-1):
			if isPalindrome(left*right):
				largestPalindrome = left*right
				break
		if largestPalindrome is not None:
			break
	print(largestPalindrome)


if __name__=="__main__":
	main()