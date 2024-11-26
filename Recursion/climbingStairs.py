def Climbing(n):
    # base case
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    # recursion relation
    steps = Climbing(n -1 ) + Climbing(n -2)
    return steps

number = 2
answer = Climbing(number)
print(answer)