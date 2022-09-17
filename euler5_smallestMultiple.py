def main():
	smallest_multiple = None
	biggest_divisor = 20
	multiplier = 2
	while smallest_multiple is None:
		current_candidate = biggest_divisor * multiplier
		divided_evenly = True
		for i in range(biggest_divisor-1,0,-1):
			if current_candidate % i != 0:
				multiplier += 1
				divided_evenly = False
				break
		if divided_evenly:
			smallest_multiple = current_candidate
	print(smallest_multiple)

if __name__=="__main__":
	main()