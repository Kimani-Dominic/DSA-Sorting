# Insertion Sort implementation using python 

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


# Driver code to test above
arr = [67, 23, 3, 1, 9, 91]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])
it