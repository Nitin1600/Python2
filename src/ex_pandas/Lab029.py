# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a", "b", "c"]),
#      "two": pd.Series([1,2,3,4], index=["a", "b", "c", "d"])}
# df = pd.DataFrame(d)
# print(df.loc["b"])

# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a", "b", "c"]),
#      "two": pd.Series([1,2,3,4], index=["a", "b", "c", "d"])}
# df = pd.DataFrame(d)
# # print(df.iloc[2])
# print(df[2:4])

import pandas as pd
df = pd.DataFrame([[1,2], [3,4]], columns=["a", "b"])
df2 = pd.DataFrame([[5,6], [7,8]], columns=["a", "b"])
df = df._append(df2)
print(df)
df = df.drop(0)
print(df)