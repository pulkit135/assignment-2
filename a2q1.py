str="Python is a case sensitive language"
length=len(str)
print("the length of the string is",length)
rev_str=str[::-1]
print("reverse of string is:",rev_str)
slice_str=str[10:26]
print("sliced string is:",slice_str)
new_str=str.replace("a case sensitive","object oriented")
print(new_str)
index_str=str.index("a")
print(index_str)
rep_str=str.replace(" ", "")
print(rep_str)



name=input("Enter your name here ")
dep_name=input("Enter your department here ")
sid=input("Enter your sid here ")
cgpa=input("Enter your cgpa here ")
print("Hey,",name," Here !")
print("My SID is",sid)
print("I am from",dep_name,"department and my CGPA is",cgpa)




a=56
b=10
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>4)




str=input("Enter a string here")
if 'name' in str:
    print("Yes")
else:
    print("No")
        



a=int(input("Enter a number"))
b=int(input("Enter a number"))
flips=0
while(a>0 and b>0):
    t1=a&1
    t2=b&1
    if(t1!=t2):
        flips+=1

        a>>=1
        b>>=1

        print("Total flips required is",flips)
