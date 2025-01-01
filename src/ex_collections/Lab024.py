from collections import Counter
# list = [1,2,3,3,4,1,1,2,3,3,4,5,5]
# cnt = Counter(list)
# print(cnt[1])

# cnt = Counter({1:3,2:4})
# print(list(cnt.elements()))
# print(list(cnt.most_common()))

# list1 = [1,2,3,2,1,2,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4]
# cnt = Counter(list1)
# print(list(cnt.most_common()))

# cnt = Counter({1:3,2:4})
# print(cnt)
# deduct = {1:1,2:2}
# cnt.subtract(deduct)
# print(cnt)

from collections import defaultdict
# nums = defaultdict(int)
# nums['one'] = 1
# nums['two'] = 2
# print(nums['three'])

from collections import defaultdict
#
# count = defaultdict(int)
# names_list = "Mike, Anna, Brit, Span, Howrah, Oliviya, Gardania, Brit, Anna, Anna, Anna, Mike, Mike, Span".split()
# for name in names_list:
#     count[name] += 1
# print(count)

# from collections import OrderedDict
# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# print(od)
#
# for key, value in od.items():
#     print(key,value)

# from collections import Counter
# from collections import OrderedDict
# list = ['a','b','c','c','b','a','d','g','b','a','c','a','b','c']
# cnt = Counter(list)
# od = OrderedDict(cnt.most_common())
# for key, value in od.items():
#     print(key,value)

# from collections import deque
# list = ["a","b","c"]
# deq = deque(list)
# print(deq)
# deq.append("d")
# deq.appendleft("e")
# print(deq)
# deq.pop()
# deq.popleft()
# print(deq)

# from collections import deque
# list = ["a", "b", "c"]
# deq = deque(list)
# # print(deq)
# # print(deq.clear())
# print(deq.count("a"))

# from collections import ChainMap
# dict1 = {'a':1, 'b':2}
# dict2 = {'c':3, 'b':4}
# chain_map = ChainMap(dict1,dict2)
# # print(chain_map.maps)
# # print(chain_map['a'])
# # dict2['c'] = 5
# # print(chain_map.maps)
# # print(list(chain_map.keys()))
# # print(list(chain_map.values()))
# dict3 = {"f":6, "e":7}
# new_chain_map = chain_map.new_child(dict3)
# print(new_chain_map)

from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '17')
print(s1.fname,s1.lname,s1.age)
s2 = Student._make(['Adam', 'Joe', '18'])
print(s2)
s3 = s1._asdict()
print(s3)
s3 = s1._replace(age='24')
print(s1)
print(s3)