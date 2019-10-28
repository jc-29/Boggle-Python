def fibonacci(num): #using loops
    start=[0, 1]
    while num >= len(start):
        start.append(start[-1] + start[-2]) 
    print(start[-1])

fibonacci(8)

# def fibonacci_recursion(num): #using recursion
#     if num <= 1:
#         return num 
#     else:
#         return (fibonacci_recursion(num - 1) + fibonacci_recursion(num-2))

# print(fibonacci_recursion(40))