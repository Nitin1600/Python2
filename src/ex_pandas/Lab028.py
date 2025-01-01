# import pandas as pd
# df = pd.DataFrame()
# print(df)

# import pandas as pd
# data = [1,2,3,4,5]
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = [["Alex", 25], ["Bob", 29], ["Clarke", 34]]
# df = pd.DataFrame(data, columns=("Name", "Age"))
# print(df)

# import pandas as pd
# data = [["Alex", 29], ["Bob", 29], ["Clarke", 34]]
# df = pd.DataFrame(data, columns=["Name", "Age"], dtype=float)
# print(df)

# import pandas as pd
# data = {"Name":["Tom", "Jerry", "Riky", "Alex"], "Age":[25, 29, 34, 39]}
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = {"Name":["Tom", "Alex", "Karry", "Bob"], "Age":[25, 29, 34, 39]}
# df = pd.DataFrame(data, index=["rank1", "rank2", "rank3"])
# print(df)

# import pandas as pd
# data = [{"a":1, "b":2}, {"a":3, "b":4, "c":5}]
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = [{"a":1, "b":2}, {"a":3, "b":4, "c":5}]
# df = pd.DataFrame(data, index = ["first", "second"])
# print(df)

# import pandas as pd
# data = [{"a":1, "b":2}, {"a":3, "b":4, "c":5}]
# df1 = pd.DataFrame(data, index=["first", "second"], columns=["a", "b"])
# df2 = pd.DataFrame(data, index=["first", "second"], columns=["a", "b1"])
# print(df1)
# print(df2)

# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a", "b", "c"]),
#      "two": pd.Series([1,2,3,4], index=["a", "b", "c", "d"])}
# df = pd.DataFrame(d)
# print(df)

# import pandas as pd
# d = {"one" : pd.Series([1,2,3], index=["a", "b", "c"]),
#       "two" : pd.Series([1,2,3,4], index=["a", "b", "c", "d"])}
# df = pd.DataFrame(d)
# print(df["one"])

# import pandas as pd
# d = {"one" : pd.Series([1,2,3], index=["a", "b", "c"]),
#      "two" : pd.Series([1,2,3,4], index=["a", "b", "c", "d"])}
# df = pd.DataFrame(d)
# print(df)
#
# df["three"] = pd.Series([10,20,30,40], index=["a", "b", "c", "d"])
# print(df)
# df["four"] = df["one"] + df["three"]
# print(df)

import pandas as pd
d = {"one": pd.Series([1,2,3], index=["a", "b", "c"]),
     "two": pd.Series([1,2,3,4], index=["a", "b", "c", "d"]),
     "three": pd.Series([10,20,30], index=["a","b","c"])}

df = pd.DataFrame(d)
print("Our dataframe is: ")
print(df)
print("Deleting column one by del function: ")
del(df["one"])
print(df)
print("Deleting column two by pop function: ")
df.pop("two")
print(df)