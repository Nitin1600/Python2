# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument("num1", help="first number")
# parser.add_argument("num1", help="second number")
# parser.add_argument("operation", help="operation")
#
# args = parser.parse_args()
# print(args.num1)
# print(args.num2)
# print(args.operation)
#
# n1 = int(args.num1)
# n2 = int(args.num2)
#
# result = n1+n2
# print("The result is: ", result)

# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument("num1", help="first number")
# parser.add_argument("num2", help="second number")
# parser.add_argument("operation", help="operation")
#
#
# args = parser.parse_args()
# print(args.num1)
# print(args.num2)
# print(args.operation)
#
# n1 = int(args.num1)
# n2 = int(args.num2)
#
# if args.operation == "add":
#     result = n1 + n2
#     print("The result is: ",result)
#
# elif args.operation == "sub":
#     result = n1 - n2
#
# elif args.operation == "mul":
#     result = n1 * n2
#
# elif args.operation == "div":
#     result = n1 / n2
#
# else:
#     print("Unmatched operation")
#
# print("The result is: ", result)

# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument("num", help="Enter number to get square of it:", type=str)
#
# args = parser.parse_args()
# # num = str("num")
# print(args.num ** 2)

# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument("num", help="Enter number to get square of it:", type=int)
#
# args = parser.parse_args()
#
# print(args.num ** 2)

# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument("--num1", help="first operation")
# parser.add_argument("--num2", help="second number")
# parser.add_argument("--operation", help="operation")
#
# args = parser.parse_args()
#
# print(args.num1)
# print(args.num2)
# print(args.operation)
#
# n1 = int(args.num1)
# n2 = int(args.num2)
#
# if args.operation == "add":
#     result = n1 + n2
#
# elif args.operation == "sub":
#     result = n1 - n2
#
# elif args.operation == "mul":
#     result = n1 * n2
#
# elif args.operation == "div":
#     result = n1 / n2
#
# else:
#     print("Unmatched argument")
#
# print("The result is: ", result)

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("example")
# args = parser.parse_args()
#
# if args.example == "Hello Python":
#     print("Welcome to World")
# else:
#     print("Didn't make it")