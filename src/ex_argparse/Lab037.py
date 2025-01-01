# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("example", default="How are you?")
# args = parser.parse_args()
# if args.example == "Hello Python":
#     print("Welcome to world")
# else:
#     print("Didn't make it")

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("-tut", "--tutorial", help="Best tutorial")
# parser.add_argument("-w", "--writer", help="Technical content")
# args = parser.parse_args()
#
# if args.tutorial == "Hello":
#     print("Welcome to the world")
#
# if args.writer == "Devansh":
#     print("Technically strong")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("tutorial", help="Best tutorial")
parser.add_argument("-w", "--writer", help="Technical content")
args = parser.parse_args()

if args.tutorial == "Hello":
    print("Welcome to the world")

if args.writer == "Devansh":
    print("Technically strong")

