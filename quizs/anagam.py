str1=input("enter the string:")
str2=input("enter the string:")
n1=len(str1)
n2=len(str2)
if n1!=n2:
    print("false")
str1=sorted(str1)
str2=sorted(str2)
if str1==str2:
    print("true")
