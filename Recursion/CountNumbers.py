def findletter(n, arr):
    #Base Case
    if n == 0:
        return True

    #processing
    digit = n % 10
    n = n // 10

    #Recursive call
    findletter(n, arr)

    #printing the number out
    print(arr[digit])


Letters = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
number = int(input("Enter a number: "))

findletter(number, Letters)
