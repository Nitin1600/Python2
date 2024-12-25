# a = 5
# def abc():
#     b=10
#     print(b)
# print(a)
# abc()

# a = 5
# def sum():
#     print(a)
# print(a)
# sum()

# a = 5
# def sum():
#     a = a + 2
#     print(a)
# print(a)
# sum()

# a = 5
# def sum():
#     global a
#     a = a + 2
#
# print(a)
# sum()
# print(a)

# def foo():
#     x = 20
#     def bar():
#         global x
#         x = 25
#         #print(x)
#     print("Before calling bar: ",x)
#     print("Calling bar now")
#     bar()
#     print("After calling bar: ", x)
#
# #(x)
# foo()
# print("x in main: ",x)

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: ",x)

    inner()
    print("outer: ",x)
outer()

# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#     inner()
#     print("a", x)
# outer()