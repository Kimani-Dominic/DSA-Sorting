#counting sort array

def countingArray(arr):
    max_num = max(arr)
    count = [0] * (max_num + 1)

    # Counting Phase
    for num in arr:
        count[num] += 1

    # Calculate Starting Index in Sorted Array
    start = [0] * (max_num + 1)
    start[0] = 0
    for i in range(1, max_num + 1):
        start[i] = start[i - 1] + count[i - 1]

    # Output Phase
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        count[arr[i]] -= 1
        output[start[arr[i]] + count[arr[i]]] = arr[i]

    return output, start

# Example Usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr, start_array = countingArray(arr)
print("Unsorted Array:", arr)
print("Sorted Array:", sorted_arr)