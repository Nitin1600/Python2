# f = open ("data.txt3", "w", encoding="cp1252")
# f.write("This is my first line\n")
# f.write("This is my second line\n")
# f.write("This is my third line")
# f.close()

# f = open("data.txt3", "r", encoding="cp1252")
# print(f.read())
# f.close()

# f = open("data.txt3", "r")
# for line in f:
#     print(line, end="")
# f.close()

# try:
#     f = open("data.txt3", "r", encoding="cp1252")
#     print(f.read())
# finally:
#     f.close()

# with open ("data.txt3", "r", encoding="cp1252") as f:
#     print(f.read())

# with open("data.txt3", "r", encoding="cp1252") as f:
#     print(f.read(4))
#     print(f.read(4))
#     print(f.tell())
#     f.seek(0)
#     print(f.read())

# with open ("data.txt3", "r", encoding="cp1252") as f:
#     print(f.readline())
#     print(f.readline())
#     f.seek(0)
#     print(f.readlines())

# with open ("data.txt3", "a", encoding="cp1252") as f:
#     # f.write("\n This is fourth line")
#     f.close()

# with open ("data.txt3", "x", encoding="cp1252") as f:
#     f.write("\nThis is my fifthh line")