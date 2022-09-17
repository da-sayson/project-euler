def main():
	r = 0
	for value in range(1000):
		if value % 3 == 0:
			r+=value
		elif value % 5 == 0:
			r+=value
	print(r)

if __name__=="__main__":
	main()