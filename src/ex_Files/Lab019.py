# f = open("data.txt", "w", encoding="cp1252")
# f.write("This is first line\n")
# f.write("This is second line\n")
# f.close()

# f = open("data.txt", "r")
# print(f.read())
# f.close()

# try:
#     f = open("data.txt", "r", encoding="cp1252")
#     print(f.read())
# finally:
#     f.close()

# with open("data.txt", "r") as f:
#     print(f.read())

# with open("data.txt", "a") as f:
#     f.write("This is first with operation\n")
#     f.write("This is second with operation\n")
#     f.write("This is third with operation\n")
#     f.close()

# with open("data.txt", "r") as f:
#     print(f.tell())
#     print(f.seek(10))
#     print(f.read())
#     f.close()

# with open ("data.txt", "r") as f:
#     print(f.read(4))
#     print(f.read(4))
#     print(f.read(10))
#     print(f.tell())
#     f.close()

# with open ("data.txt", "r", encoding="cp1252") as f:
#     print("1st line->", f.readline())
#     print("2nd line->", f.readline())
#     print("3rd line->", f.readline())
#     print("4th line->", f.readline())
#     f.close()

# with open ("data.txt2", "x", encoding="cp1252") as f:
#     f.write("This is test exclusive creation")
#     f.close()

try:
    with open("data.txt", "x", encoding="cp1252") as f:
        f.write("This is test exclusive creation2")
        f.close()
except FileExistsError:
    print("File already exists")