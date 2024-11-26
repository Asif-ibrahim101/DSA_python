# # first Recursive function
# def Factorial(n):
#     # Base Case
#     if n == 0:
#         return 1
    
#     # recursive relation
#     Answer = n * Factorial(n -1)
#     return Answer

# number = 5;
# Result = Factorial(number)

# print(Result)

# # Second Resurssive function
# def Power(n):
#     # base case
#     if n == 0:
#         return 1
    
#     # Recurssive Relation
#     Answer = 2 * Power(n -1)
#     return Answer

# number = 3;
# answer = Power(number)

# print(answer)

# # Thried Reccursive function
# def Counting(n):
#     # base case
#     if n == 1:
#         print(1)
#         return
    
#     # recursive relation
#     Counting(n - 1)
#     print(n)

# number = 10
# Counting(number)

# fourth Recursion function
def ReachHome(src, dest):
    print("Source ", src, "destination ", dest)
    # Base Case
    if (src == dest):
        print("Already there")
        return True;
    
    # Recurstion Relation
    result = ReachHome(src + 1, dest)
    return result
    
dest = 10;
src = 1;

Answer = ReachHome(src, dest)
print(Answer)
