# class CustomError(Exception):
#     pass
# #
# # raise CustomError
#
# raise CustomError("An error occured")

# class Error(Exception):
#     pass
# class ValueTooSmallError(Error):
#     pass
# class ValueTooLargeError(Error):
#     pass
#
# number = 10
# while True:
#     try:
#         i_num = int(input("Guess the correct number: "))
#         if i_num < number:
#             raise ValueTooSmallError
#         elif i_num > number:
#             raise ValueTooLargeError
#         break
#     except ValueTooSmallError:
#         print("Oops! Value too small, try again!")
#         print()
#     except ValueTooLargeError:
#         print("Oops! Value too large, try again!")
#         print()
# print("Congratulations!, you guessed it right")

# class SalaryNotInRangeError(Exception):
#
#     def __init__(self, salary, message="Salary is not in (5000,15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)
#
# salary = int(input("Enter the salary: "))
# if not 5000 <= salary <= 15000:
#     raise SalaryNotInRangeError(salary)

# class SalaryNotInRangeError(Exception):
#
#     def __init__(self, salary, message="Salary is not in (5000,15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)
#
#     def __str__(self):
#         return f'{self.salary} -> {self.message}'
#
# salary = int(input("Enter the salary: "))
# if not 5000 <= salary <= 15000:
#     raise SalaryNotInRangeError(salary)

class InvalidageException(Exception):

class License(InvalidageException):
    age=14
    if age >= 18:
        print("Eligible")
    else:
        try:
            raise InvalidageException("Age is not valid")
        except InvalidageException as e:
            print(e)