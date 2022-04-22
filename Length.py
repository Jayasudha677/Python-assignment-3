str="python"
print(len(str))
#using for loop
def stringLength(str):
     count=0
     for i in str:
          count+=1
          return count
str="h"
print(stringLength(str))
#using while loop
def stringlength(str):
     count=0
     while str[count:]:
          count +=1
     return count
str="j"
print(stringLength(str))
#using join
def stringlength(str):
     if not str:
          return 0
     else:
          some_random_str='words'
          return ((some_random_str).join(str)).count(some_random_str)+1
str="a"
print(stringLength(str))