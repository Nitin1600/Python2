# def PowTwoGen(max=0):
#     n=0
#     while n < max:
#         yield 2**n
#         n += 1
#
# def all_even():
#     n=0
#     while True:
#         yield n
#         n += 2
#
# a = all_even()
# # for val in a:
#     # print(val)
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

class PowTwo:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

a = PowTwo(3)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
