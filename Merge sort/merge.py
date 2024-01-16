#Merge sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage:
my_list = input("input array to be sorted in numericals and space them: ")

numerical_values = [int(value) for value in my_list.split() if value.isdigit() or (value[0] == '-' and value [1:].isdigit())]
if len(numerical_values) == 0:
    print("input numerical values only!")
else:    
    merge_sort(numerical_values)
    print("Sorted list:", numerical_values)