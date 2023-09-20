arr = ["a", "e", "i", "o", "u"]
i = 0


arr[i] = 11
if arr[i] > 1:
	for i in range(2, int(arr[i]/2)+1):
		
		if (arr[i] % i) == 0:
			print(arr[i])