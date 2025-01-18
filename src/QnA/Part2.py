# my_list = [i for i in range(1,10)]

# a = lambda x,y : x*y
# print(a(2,4))

# string = "GeeKS"
# print(string.swapcase())

# my_dict = {i:i+7 for i in range(1,10)}
# print(my_dict)

# class GeeksClass:
#     def function(self):
#         print("Function()")
#
# import m
# def monkey_function():
#     print("monkey_function")
#
# m.GeeksClass.function = monkey_function()
# obj = m.GeeksClass()
# obj.function()

# import time
#
# current_time = time.localtime(time.time())
# print("Current time is: ", current_time)

# names=["James","Joe","Jimmy"]
#
# if (name := input("Enter your name: ")):
#     print(f"{name.upper()} is found")
# else:
#     print("Match not found")

# a = '5'; print(int(a))

# str1 = "Analytics Vidhya"
# print(list(str1.split(" ")))

# str1 = "Analytics Vidhya"
# str2 = ""
# for i in str1:
#     str2 = i + str2
# print("The original string is: ", str1)
# print("The reversed string is: ", str2)

# my_list = [3,2,1]
# my_list.sort()
# print(my_list)

# import os
# os.remove("text.txt")

# list = [1,2,3,4]
# print(list[0])
# print(list[1])

# list.clear()
# print(list.remove(2))
# print(list)
# print(list.pop(2))
# print(list.clear())
# print(list)

def atm_withdrawl(s):
    if type(s) != int:
        return "Input must be a integer"
    if s < 0:
        return "Input must be greater then zero"
    if s % 10 != 0:
        return "Input should be multiple of 10"


    hundred_count = s // 100
    balance_after_hundred = s - 100* hundred_count
    fifty_count = balance_after_hundred // 50
    balance_after_50 = balance_after_hundred - 50 * fifty_count
    ten_count = balance_after_50 // 10

    return("Money withdrawn is " + str(hundred_count) + " : 100s; " + str(fifty_count) + " : 50s; "
           + str(ten_count) + " : 10s; ")

print(atm_withdrawl(790))


