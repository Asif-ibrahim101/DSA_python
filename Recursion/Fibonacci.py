# def Febonacci(n):
#     # base case
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#
#     # reccursive relation
#     answer = Febonacci(n - 1) + Febonacci(n -2)
#     return answer
#
# number =  3
# result = Febonacci(number)
# print(result)

# Print the febonacci series upto nth time
def febonacci(n):
    # base case
    if n < 1:
        return True
    else:
        return febonacci(n-1)+febonacci(n-2)

is_taken = 10
for i in range(1,is_taken):
    print("Factorial: ", febonacci(i))