from collections import OrderedDict
def remove_duplicate(s):
     return "".join(OrderedDict.fromkeys(s))
s="abcabc"
print(s)
print("after removing duplicates:",remove_duplicate(s))