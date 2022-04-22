def CheckString(s):
     s=s.lower()
     vowels=set("aeiou")
     for char in s:
          if char in vowels:
               vowels.remove(char)

     if len(vowels)==0:
          print("accepted")
     else:
          print("not acceped")
s1="Aebideffobuw"
print(s1)
CheckString(s1)
s2="python"
print(s2)
CheckString(s2)
