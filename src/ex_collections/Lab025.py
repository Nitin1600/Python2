from collections import Counter, OrderedDict
# l = [1,2,3,4,5,6,7,8,1,2,3,4,6,7,1,2,3,4,1,2,3,4,5]
# cnt = Counter(l)
# print(cnt)
# print(cnt[7])

# cnt = Counter({1:2, 2:4})
# print(list(cnt.elements()))

# l = [1,2,3,4,5,6,7,8,1,2,3,4,6,7,1,2,3,4,1,2,3,4,5]
# cnt = Counter(l)
# print(cnt.most_common())

# cnt = Counter({1:3,2:4,3:6})
# print(type(cnt))
# deduct = {1:2,2:2}
# print(type(deduct))
# cnt.subtract(deduct)
# print(cnt)

# cnt = Counter({1:3,2:4,3:6})
# print(type(cnt))
# deduct = Counter({1:1,2:2})
# print(type(deduct))
# cnt1 = cnt.subtract(deduct)
# print(cnt1)

# l = [4,5,6]
# l1=l.reverse()
# print(l1)

# d = {'id':1, 'name':'Raj'}
# print(d['id'])

# from collections import defaultdict
# d = defaultdict(str)
# d['name'] = 'Raj'
# d['id'] = 1
# print(d['address'])

# from collections import defaultdict
# count = defaultdict(int)
# names_list = "Mike, Anna, Brit, Span, Howrah, Oliviya, Gardania, Brit, Anna, Anna, Anna, Mike, Mike, Span".split()
# print(names_list)
# for names in names_list:
#     count[names] += 1
# print(count)

from collections import OrderedDict
# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# print(od)
# for key, value in od.items():
#     print(key,value)

# l = ['a','b','c','c','b','a','d','g','b','a','c','a','b','c']
# cnt = Counter(l)
# od = OrderedDict(cnt.most_common())
# print(od)
# for key, value in od.items():
#     print(key,value)

# from collections import deque
# l = ["a","b","c"]
# deq = deque(l)
# print(deq)
# deq.append("d")
# deq.appendleft("e")
# print(deq)
# deq.pop()
# deq.popleft()
# print(deq)
# print(deq.count('c'))

# from collections import ChainMap
# dict1 = {'a':1, 'b':2}
# dict2 = {'c':3, 'b':4}
# chain_map = ChainMap(dict1,dict2)
# print(chain_map.maps)
# dict2['c'] = 5
# print(chain_map.maps)
# print(list(chain_map.keys()))
# print(list(chain_map.values()))
# dict3 = {'e':6,'f':7}
# new_chain_map = chain_map.new_child(dict3)
# print(new_chain_map)

from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '12')
print(s1)
print(s1.fname, s1.lname, s1.age)
s2 = Student._make(['Adam', 'Joe', '18'])
print(s2)
s2 = s1._asdict()
print(s2)
s2 = s1._replace(age='14')
print(s1)
print(s2)