# if a < 3
# 1/0
# open("imaginary.txt")
# print(dir(locals()['__builtins__']))

# import sys
# randomList = ["a", 0, 2]
# for entry in randomList:
#     try:
#         print("The entry is: ", entry)
#         r = 1/int(entry)
#         break
#     except:
#         print("Oops!", sys.exc_info()[0], "occured")
#         print("Next entry")
#         print()
# print("The reciprocal of", entry, "is", r)

# import sys
# randomList = ["a", 0, 2]
# for entry in randomList:
#     try:
#         print("The entry is: ", entry)
#         r = 1/int(entry)
#         break
#     except:
#         print("Oops!", sys.exc_info()[0], "occured")
#         print("Next entry")
#         print()
# print("The reciprocal of", entry, "is", r)

# import sys
# randomList = ["a", 0, 4]
# for entry in randomList:
#     try:
#         print("The entry is: ", entry)
#         r = 1/int(entry)
#         break
#     except Exception as e:
#         print("Oops!", e.__class__, "occured")
#         print("Next entry")
#         print()
# print("The reciprocal of", entry, "is", r)

# raise KeyboardInterrupt
# raise MemoryError("This is an argument")

# try:
#     a = int(input("Enter a positive number: "))
#     if a <= 0:
#         raise ValueError("This is not a positive number!")
# except ValueError as ve:
#     print(ve)

# try:
#     num = int(input("Enter thr number: "))
#     assert num % 2 == 0
# except:
#     print("Not a even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)

try:
    f = open("test.txt", encoding="utf-8")
finally:
    f.close()
