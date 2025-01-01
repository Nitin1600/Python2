# a = 10
# b = "a"
# try:
#     result = a/int(b)
#     print(result)
# except ZeroDivisionError as e1:
#     print("Error handeled: ", e1)
# except TypeError as e2:
#     print("type:", e2)
# except ValueError as e3:
#     print("value: ", e3)
# except Exception as e4:
#     print("error details:", e4)
# print("hello world")

# try:
#     f = open("test.txt", encoding = "cp1252")
#     print(f)
# except FileNotFoundError as fnfe:
#     print("file details:", fnfe)

class InvalidageException(Exception):

class License(InvalidageException):
    age = 14
    if age >= 18:
        print("Eligible")
    else:
        try:
            raise InvalidageException("Age is not valid")
        except InvalidageException as e:
            print("Eligibility:", e)
