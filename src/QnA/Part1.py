# import array
# a = array.array('i',[1,2,3])
# for i in a:
#     print(i, end=' ')
# from numpy.f2py.crackfortran import cracktypespec0
# from pandas.util import capitalize_first_letter


# def lowercase_decorator(function):
#     def wrapper():
#         func=function()
#         string_lowercase = func.lower()
#         return string_lowercase
#     return wrapper
#
# def splitter_decorator(function):
#     def wrapper():
#         func = function()
#         string_split = func.split()
#         return string_split
#     return wrapper
#
# @splitter_decorator
# @lowercase_decorator
# def hello():
#     print('Hello World')
# hello()

# def abc(function):
#     def wrapper(arg1, arg2):
#         arg1 = arg1.capitalize()
#         arg2 = arg2.capitalize()
#         string_capital = function(arg1,arg2)
#         return string_capital
#     return wrapper
#
# @abc
#
# def say_hello(name1,name2):
#     print('Hello ' + name1 + '! Hello ' + name2 + '!')
# say_hello('sara', 'hennah')

# def abc(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper
#
# def say_hello():
#     print("Hello")
# say_hello()

# my_list = [2,3,5,7,10,11]
# squared_list = [x**2 for x in my_list]
# squared_dict = {x:x**2 for x in my_list}
# print(squared_list)
# print(squared_dict)

# a=[1,2,3]
# b=[4,5,6]
# combine1 = [(x+y) for (x,y) in zip(a,b)]
# combine2 = [(x,y) for x in a for y in b]
# print(combine1)
# print(combine2)

# my_list = [2,3,5,7,10,11]
# s_l = [x**2 for x in my_list if x%2 !=0]
# s_d = {x:x**2 for x in my_list if x%2 !=0}
# print(s_l)
# print(s_d)

# my_list=[[10,20,30],[40,50,60],[70,80,90]]
# # flattened = [x for temp in my_list for x in temp]
# # print(flattened)
# for temp in my_list:
#     print(temp)
    # for x in temp:
    #     print(x)
        # x = list(x)
        # print(x)

# mul = lambda a,b : a*b
# print(mul(2,5))

# def myWrapper(n):
#     return lambda a: a*n
# mulFive = myWrapper(7)
# print(mulFive(2))

# from copy import copy, deepcopy
# list1=[1,2,[3,4],5]
# list2 = copy(list1)
# list2[3] = 6
# list2[2].append(7)
# print(list2)
# print(list1)
#
# list3 = deepcopy(list1)
# list3[3] = 8
# list3[2].append(9)
# print(list3)
# print(list1)

# for i in range(10):
#     print(i)
# for i in range(1,10):
#     print(i)
# for i in range(1,10,2):
#     print(i)

# def fib(n):
#     p,q = 0,1
#     while(p < n):
#         yield p
#         p,q=q,p+q
# x = fib(10)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# for i in fib(10):
#     print(i)

# def appendNumber(arr):
#     arr.append(4)
# arr=[1,2,3]
# print(arr)
# appendNumber(arr)
# print(arr)

# class ArrayList:
#     def __init__(self, numbers_list):
#         self.numbers = numbers_list
#
#     def __iter__(self):
#         self.pos=0
#         return self
#
#     def __next__(self):
#         if (self.pos < len(self.numbers)):
#             self.pos += 1
#             return self.numbers[self.pos - 1]
#         else:
#             raise StopIteration
# array_obj =ArrayList([1,2,3])
# it = iter(array_obj)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# string = "This is a string"
# string_list = string.split(' ')
# print(string_list)
# print(' '.join(string_list))

# def multiply(a,b, *argv):
#     mul = a * b
#     for num in argv:
#         mul *= num
#     return mul
# print(multiply(1,2,4,6,7,8))

# def tellArguments(**kwargs):
#     for key, value in kwargs.items():
#         print(key + ': ' + value)
# tellArguments(arg1= "Argument 1", arg2= "Argument 2", arg3= "Argument 3")

# class InterviewbitEmployee:
#     def __init__(self, emp_name):
#         self.emp_name = emp_name
#
#     def introduce(self):
#         print("Hello I am " + self.emp_name)
#
# emp_1 = InterviewbitEmployee("Mr.Employee")
# print(emp_1.emp_name)
# emp_1.introduce()

# class Parent:
#     def par_fun(self):
#         print("I am parent class function")
#
# class Child(Parent):
#     def child_fun(self):
#         print("I am child class function")
#
# obj1 = Child()
# obj1.par_fun()
# obj1.child_fun()

# class A:
#     def __init__(self, a_name):
#         self.a_name = a_name
#
# class B(A):
#     def __init__(self, b_name, a_name):
#         self.b_name = b_name
#         A.__init__(self, a_name)
#
# class C(B):
#     def __init__(self, c_name, b_name, a_name):
#         self.c_name = c_name
#         B.__init__(self, b_name, a_name)
#
#     def display_names(self):
#         print("A is: ", self.a_name)
#         print("B is: ", self.b_name)
#         print("C is: ", self.c_name)
#
# obj1 = C("child", "intermediate", "parent")
# print(obj1.a_name)
# obj1.display_names()

# class Parent1:
#     def parent1_func(self):
#         print("I am first parent")
#
# class Parent2:
#     def parent2_func(self):
#         print("I am second parent")
#
# class Child(Parent1, Parent2):
#     def child_func(self):
#         self.parent1_func()
#         self.parent2_func()
#
# obj1 = Child()
# obj1.child_func()

# class A:
#     def a_name(self):
#         print("I am Parent")
#
# class B(A):
#     def b_name(self):
#         print("I am first child")
#
# class C(A):
#     def c_name(self):
#         print("I am second child")
#
# obj1 = B()
# obj2 = C()
# obj1.a_name()
# obj1.b_name()
# obj2.a_name()
# obj2.c_name()

# class Parent:
#     def __init__(self, name):
#         self.name = name
#
# class Child(Parent):
#     def __init__(self, name, age):
#         Parent.name = name
#         self.age = age
#
#     def display(self):
#         print(Parent.name, self.age)
#
# obj1 = Child("Bit", 6)
# obj1.display()

# class Parent(object):
#     def __init__(self, name):
#         self.name = name
#
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age=age
#
#     def display(self):
#         print(self.name, self.age)
#
# obj = Child("bit", 6)
# obj.display()


# class BitEmployee:
#     _emp_name=None
#     _age=None
#     __branch=None
#
#     def __init__(self, emp_name, age, branch):
#         self._emp_name=emp_name
#         self._age=age
#         self.__branch=branch
#
#     def display(self):
#         print(self._emp_name+" "+self._age+" "+self.__branch)
#
# obj = BitEmployee()

# class EmptyClass:
#     pass
# obj=EmptyClass()
# obj.name="Bit"
# print("Object created = ", obj.name)

# class Bit:
#     def __init__(self,emp_name):
#         self.emp_name=emp_name
#
#     def display(self):
#         print("Hello I am", self.emp_name)
#
# obj=Bit("Mr.Employee")
# obj.display()

# class Parent(object):
#     pass
#
# class Child(Parent):
#     pass
#
# obj1=Child()
# obj2=Parent()
# print(issubclass(Parent, Child))
# print(issubclass(Child, Parent))
#
# print(isinstance(obj2, Parent))
# print(isinstance(obj2, Child))

# import pandas as pd
# df1 = pd.DataFrame(data, index, columns, dtype)
# df1.append(df2)
# pd.concat([df1, df2])
# df1.join(df2)

# import pandas as pd
# dict_info={'key1':2.0, 'key2': 4.8, 'key3': 3.4}
# series_obj=pd.Series(dict_info)
# print(series_obj)

# missing=df.isnull().sum()
# pd['column_name'].fillna(0)
# pd['column_name'] = pd.['column_name'].fillna((pd['column_name'].mean()))

# import pandas as pd
# data_info = {'first': pd.Series([1,2,3], index=['a', 'b', 'c']),
#              'second': pd.Series([4,5,6,7], index=['a', 'b', 'c', 'd'])}
# df=pd.DataFrame(data_info)
# df['third'] = pd.Series([10,20,30], index=['a', 'b', 'c'])
# print(df)
# df['fourth']=df['first']+df['third']
# print(df)

# df.index.name=None
# del df.index.name)
# print(df)

# import pandas as pd
# df1 = pd.Series([2,4,10,8,12])
# df2 = pd.Series([8,10,12,15])
# df1 = df1[-df1.isin(df2)]
# print(df1)

# import pandas as pd
# import numpy as np
# df1 = pd.Series([1,2,3,4,5])
# df2 = pd.Series([3,4,5,6,7,8])
# p_union=pd.Series(np.union1d(df1,df2))
# p_intersection=pd.Series(np.intersect1d(df1,df2))
# unique_elements = p_union[-p_union.isin(p_intersection)]
# print(unique_elements)

# import pandas as pd
# import numpy as np
# dateparser = lambda date_val: datetime.strptime(date_val, '%Y-%m-%d %H:%M:%S')
# df = pd.read_csv("somefile.csv", parse_dates=['datetime_columns'], date_parser=dateparser())
# print(df)

# import pandas as pd
# import numpy as np
# one_dimensional_list=[1,2,3]
# one_dimensional_arr = np.array(one_dimensional_list)
# print("1D array is: ", one_dimensional_arr)

# import pandas as pd
# import numpy as np
# two_dimensional_list = [[1,2,3],[4,5,6]]
# two_dimensional_arr = np.array(two_dimensional_list)
# print("2D array is:",two_dimensional_arr)

# import numpy as np
# three_dimensional_list = [[1,2,3],[4,5,6],[7,8,9]]
# three_dimensional_arr = np.array(three_dimensional_list)
# print("3D array is:",three_dimensional_arr)

# import numpy as np
# ndArray = np.array([1,2,3,4], ndmin=6)
# print(ndArray)
# print("Dimension of array: ", ndArray.ndim)

# import numpy as np
# inputarray = np.array([[35,53,63], [72,12,22], [43,84,56]])
# new_col=np.array([[20,30,40]])
# arr=np.delete(inputarray, 1, axis=1)
# arr=np.insert(arr,1, new_col, axis=1)
# print(arr)

# from numpy import genfromtxt
# csv_data = genfromtxt('simple_file.csv', delimiter=',')

# import pandas as pd
# import numpy as np
# arr=np.array([[8,3,2],
#               [3,6,5],
#               [6,1,4]])
# arr=np.sort(arr.view('i8,i8,i8'),
#             order=['f1'],
#             axis=0)
# arr.view('i8,i8,i8').sort(order=['f1'],axis=0)

# import numpy as np
# def find_nearest_value(arr, value):
#     arr=np.asarray(arr)
#     idx=(np.abs(arr-value)).argmin()
#     return arr[idx]
# arr=np.array([0.21169, 0.61391, 0.6341, 0.0131, 0.16541, 0.5645, 0.5742])
# value=0.52
# print(find_nearest_value(arr, value))

# reversed_array = arr[::-1]
# print(reversed_array)

# import numpy as np
# arr_two_dim = np.array([("x1","x2","x3","x4"),
#                 ("x5","x6","x7","x8")])
# arr_one_dim = np.array([(3,2,4,5,6)])
# print("2D Array Shape: ", arr_two_dim.shape)
# print("1D Array Shape: ", arr_one_dim.shape)

# mul_fun=lambda x,y:x*y
# print(mul_fun(6,4))

# import random
# # print(random.random())
# print(random.randrange(5,100,2))

# print("abcd1234".isalnum())
# print("abcd@1234".isalnum())
# import re
# print(bool(re.match('[A-Za-z0-9]+$', 'abcd1234')))
# print(bool(re.match('[A-Za-z0-9]+$', 'abcd@1234')))

# def main():
#     print("Hi bit!")
# if __name__=="__main__":
#     main()

# def function_name(*arg_list):
# def func(*var):
#     for i in var:
#         print(i)
# func(1)
# func(20,1,6)

# def check_distinct(data_list):
#     if len(data_list) == len(set(data_list)):
#         return True
#     else:
#         return False
#
# print(check_distinct([1,2,3,4,5]))
# print(check_distinct([2,2,4,4,5,6]))

# import collections
# import pprint
# with open("sample_file.txt", "r") as data:
#     count_data = collections.Counter(data.read().upper())
#     count_value = pprint.pformat(count_data)
#     print(count_value)

# def print_pair(arr, N):
#     hash_set = set()
#
#     for i in range(0, len(arr)):
#         val = N-arr[i]
#         if (val in hash_set):
#             print("Pairs " + str(arr[i]) + ", " + str(val))
#         hash_set.add(arr[i])
#
# arr=(1,2,3,4,5,6)
# N=10
# print_pair(arr, N)

# def add_nums(num1, num2):
#     while num2 != 0 :
#         data = num1 & num2
#         num1 = num1 ^ num2
#         num2 = data << 1
#     return num1
#
# print(add_nums(2,10))

# ax+by = c
# mx+ny = 0

# a,b,c,m,n,o = 5,9,4,7,9,4
# temp = a*n - b*m
# if n != 0:
#     x=(c*n - b*o) / temp
#     y=(a*0 - b*m) / temp
#     print(str(x) + str(y))

# import re
# def match_text(txt_data):
#     pattern = "ab{4,8}"
#     if re.search(pattern, txt_data):
#         return "Match Found"
#     else:
#         return "Match not Found"
# print(match_text("abc"))
# print(match_text("aabbbbbc"))

# import re
# def format(date):
#     return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
# date_input= "2021-08-01"
# print(format(date_input))

# from datetime import datetime
# new_date = datetime.strptime("2021-08-01", "%Y-%m-%d").strftime("%d-%m-%Y")
# print(new_date)

# from collections import Counter
# d1 = {"key1":50, "key2":100, "key3":200}
# d2 = {"key1":60, "key2":100, "key4":300}
# new_dict = Counter(d1) + Counter(d2)
# print(new_dict)

# import pandas as pd
# from io import StringIO
# csv_link = "https://docs.google.com/spreadsheet/d...."
# data_source = StringIO.StringIO(requests.get(csv_link).content)
# dataframe = pd.read_csv(data_source)
# print(dataframe.head())

# print(1300//500)
def atm_withdrawl(s):
    Available_denominations_in_list_formate = [2000, 500, 100]
    if type(s) != int:
        return "Input must be a integer"
    if s < 0:
        return "Input must be greater then zero"
    if s % 100 != 0:
        return "Input should be multiple of 100"

    two_thousand_count = s // 2000
    balance_after_two_thousand_count = s - 2000 * two_thousand_count
    five_hundred_count = balance_after_two_thousand_count // 500
    balance_after_500 = balance_after_two_thousand_count - 500 * five_hundred_count
    two_hundred_count = balance_after_500 // 200
    balance_after_200 = balance_after_500 - 200 * two_hundred_count
    one_hundred_count = balance_after_200 // 100

    return (dict(two_thousand_count=f"{two_thousand_count}", five_hundred_count=f"{five_hundred_count}",
            two_hundred_count=f"{two_hundred_count}", one_hundred_count=f"{one_hundred_count}"))

print(atm_withdrawl(5300))