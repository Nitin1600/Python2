# my_list = [4,7,0,3]
# my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))
# print(my_iter.__next__())
# print(my_iter.__next__())

# for element in my_list:
#     print(element)

iterable = [4,5,6,7]
my_iter = iter(iterable)

# while True:
#     try:
#         element = next(my_iter)
#         print(element)
#     except StopIteration:
#         break

class PowTwo:

    def __init__(self,max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# numbers = PowTwo(3)
# i = iter(numbers)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# # print(next(i))
for i in PowTwo(5):
    print(i)

