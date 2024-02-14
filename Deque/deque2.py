def max_of_subarrays(arr, k):
    result = []
    max_values = []

    for i in range(len(arr)):
        while max_values and max_values[0] < i - k + 1:
            max_values.pop(0)

        while max_values and arr[max_values[-1]] < arr[i]:
            max_values.pop()

        max_values.append(i)

        if i >= k - 1:
            result.append(arr[max_values[0]])

    return result

# Example usage
arr = [1, 2, 6, 1, 4, 5, 2, 3, 6]
K = 3
output = max_of_subarrays(arr, K)
print(output)
