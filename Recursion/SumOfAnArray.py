def Sum(arr, len):
    sum = 0
    for i in range(len):
        sum += arr[i]

    return sum

arr = [3, 2, 5, 1 , 6]
size_arr = len(arr)
result = Sum(arr, size_arr)
print(result)

# Summ of the array using recurssion
def Recursion_sum(arr, index=0):
    # Base case - when index reaches end of array
    if index == len(arr):
        return 0

    # Recursive relation: current element + sum of rest of array
    return arr[index] + Recursion_sum(arr, index + 1)


arr = [3, 2, 5, 1, 6]
print(Recursion_sum(arr))  # Output: 17