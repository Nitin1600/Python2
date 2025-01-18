# x= [x for x in range(5)]
# print(x)
#
# y = [y : y+2 for y in range(5)]
# print(y)

# l=[1,2,3,4,5,6,7,8]
# print(l[-1:-4:2])

# a = 2
# def add():
#     b = 3
#     c = a + b
#     print(c)
#     print(b)
# add()
# print(b)

# import array as arr
# My_Array = arr.array('i',[1,2,3,4])
# My_list = [5,6,7,8]
# print(My_Array)
# print(My_list)

# def NewFunc():
#     print("Hi, Welcome to Edurekha")
# NewFunc()

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = 20000
#
# E1 = Employee("XYZ", 25, 20000)
# print(E1.name)
# print(E1.age)
# print(E1.salary)

# a = lambda x, y : x + y
# print(a(5,6))

# import array as arr
# My_Array=arr.array('i',[1,2,3,4])
# print(My_Array[::-1])
# print(My_Array)

# from random import shuffle
# x = ["keep", "the", "blue", "flag", "high"]
# # shuffle(x)
# print(x)

# """
# Using docstrings as comments,
# this code divides two numbers
# """
# x=4
# y=2
# z=x/y
# print(z)

# dict = {"Country":"India", "Capital":"New_Delhi", "PM":"Modi"}
# print(dict["Country"])
# print(dict["Capital"])
# print(dict["PM"])

# x,y =25,50
# big = x if x<y else y
# print(big)

# stg = "ABCD"
# print(stg.lower())
# print(stg.upper())
# print(len(stg))

# a = "string"
# print(a[::-1])

# import os
# os.remove("sample_file.txt")

# import array as arr
# a = arr.array('d',[1.1,2.2])
# a.append(3.3)
# print(a)
# a.extend([4.4,5.5,6.6])
# print(a)
# a.insert(2,7.7)
# print(a)

# import array as arr
# a = arr.array('d',[1.1, 2.2, 7.7, 3.3, 4.4, 5.5, 6.6])
# print(a.pop())
# print(a.pop(3))
# a.remove(1.1)
# print(a)

# a = "edureka python"
# print(a.split())
# "  ".join(a)
# print(a)

# words = "Nitin"
# count = {}
# for char in words.lower():
#     if char in count:
#         count[char]+=1
#     else:
#         count[char] = 1
# print(count)

# def swapPositions(list, pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list
#
# List = [19, 45, 43, 78]
# pos1, pos2 = 2, 1
# print(swapPositions(List, pos1-1, pos2-2))

# class Employee:
#     def __init__(self, name):
#         self.name = name
# E1=Employee("abc")
# print(E1.name)

# class MyClass:
#     def f(self):
#         print("f()")
#
# import m
# def monkey_f(self):
#         print("monkey_f()")
#
# m.MyClass.f = monkey_f
# obj = m.MyClass
# obj.f()

# class a:
#     pass
# obj = a()
# obj.name = "xyz"
# print("Name=",obj.name)

# import pandas as pd
# data = {"Fruits":["Apple","Banana","Orange"], "Quantity":[4,3,5]}
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# ser_data = {"A":5, "B":10, "C":15, "D":20, "E":25}
# ser = pd.Series(ser_data)
# print(ser)

"""Scenario :
ATM Machine Transaction

Inputs :
1. Amount to be withdrawn - int
2. List of denominations available - list

Expected Output :
Dictionary of Denomination as Key and Count of each Denomination as Value, such that total of all should be equal to amount requested 

Constrains :
For any amount entered, maximum number of nearest largest available denomination should be chosen.
Example :
If Amount entered is Rs.5,300, and all Denominations are available,
Then, output dictionary will be like :
{2000:2, 500:2, 200:1, 100:1},

If Amount entered is 300,
Output Dictionary will be like :
{200:1, 100:1}
If Denomination available is only 100, 50, then, Output Dictionary will be like :
{100:3}"""

def atm_withdrawl(s):
    Available_denominations = [2000, 500, 100]
    if type(s) != int:
        return "Input must be a integer"
    if s < 0:
        return "Input must be greater then zero"
    if s % 100 != 0:
        return "Input should be multiple of 100"


    two_thousand_count = s // 2000
    balance_after_two_thousand_count = s - 2000* two_thousand_count
    five_hundred_count = balance_after_two_thousand_count // 500
    balance_after_500 = balance_after_two_thousand_count - 500 * five_hundred_count
    two_hundred_count = balance_after_500 // 200
    balance_after_200 = balance_after_500 - 200 * two_hundred_count
    one_hundred_count = balance_after_200 // 100

    return("Money withdrawn is -> " + str(two_thousand_count) + "*2000s; "+ str(five_hundred_count) + ":*500s; " +
           str(two_hundred_count) + ":*200s; " +  str(one_hundred_count) + ":*100s")

print(atm_withdrawl(5900))



















