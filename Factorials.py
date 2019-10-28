# def factorials(num):
#     if num == 1:
#         return num
#     elif num == 0:
#         return 1
#     else: 
#         return num * factorials(num-1)

# print(factorials(0))

def factorials(num):
    # pre = num - 1 
    num_list = list(range(1, num+1))
    i = 0
    answer = 1
    while i < num:
        answer = answer * num_list[i]
        i+=1
    return answer

print(factorials(0))

