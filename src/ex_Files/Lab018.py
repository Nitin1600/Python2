# try:
#     f = open("test.txt", mode="w", encoding="cp1252")
# finally:
#     f.close()

# with open ("test.txt", encoding="cp1252") as f:

# with open("test.txt2", "w", encoding="utf-8") as f:
#     f.write("This is first file\n")
#     f.write("My file\n\n")
#     f.write("Three statements\n")
# f.close()

f=open("test.txt2", 'r', encoding='cp1252')
# print(f.read(4))
# print(f.read(4))
# # print(f.read())
# print(f.tell())
# print(f.seek(120))
# print(f.read(4))
# print(f.read())
# for line in f:
#     print(line, end="")
# print(f.readline())
# print(f.readline())
# print(f.readline())
print(f.readlines())
# print(f.readline())
