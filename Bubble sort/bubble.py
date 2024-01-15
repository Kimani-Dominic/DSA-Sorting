
#bubble sort algorithmn 
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                
my_list = input("Enter an array of space-separated numerical values: ")

numeric_values = [int(value) for value in my_list.split() if value.isdigit() or (value[0] == '-' and value[1:].isdigit())]

if len(numeric_values) == 0:
    print("No numerical values entered.")
else:
    bubble_sort(numeric_values)
    print("Sorted list:", numeric_values)