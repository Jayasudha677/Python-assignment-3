def remove_char(s,i):
     a=s[ : i]
     b=s[i +1:]
     return a+b
string="pythonworld"
i=5
print(remove_char(string,i-1))