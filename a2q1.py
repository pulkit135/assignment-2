str="Python is a case sensitive language"
length=len(str)     #part a
print("the length of the string is",length)
rev_str=str[::-1]   #part b
print("reverse of string is:",rev_str)
slice_str=str[10:26]    #part c
print("sliced string is:",slice_str)
new_str=str.replace("a case sensitive","object oriented")
print(new_str)      #part d
index_str=str.index("a")
print(index_str)   #part e
rep_str=str.replace(" ", "")
print(rep_str)  #part f



name=input("Enter your name here ")
dep_name=input("Enter your department here ")
sid=input("Enter your sid here ")
cgpa=input("Enter your cgpa here ")
print("Hey,",name," Here !")
print("My SID is",sid)
print("I am from",dep_name,"department and my CGPA is",cgpa)




a=56
b=10
print(a&b)  #part a
print(a|b)  #part b
print(a^b)  #part c
print(a<<2) #part d
print(b<<2) #part e
print(a>>2) #part f
print(b>>4) #part g




str=input("Enter a string here")
if 'name' in str:
    print("Yes")
else:
    print("No")



side1=round(float(input('Enter first side : ')))
side2=round(float(input('Enter second side : ')))
side3=round(float(input('Enter third side : ')))
a=side1+side2>side3
b=side2+side3>side1
c=side3+side1>side2
match a,b,c:
    case True,True,True:            # Checking for valid triangle case
        print('Yes')
    case (False,True|False,True|False)|(True,False,True|False)|(True,True,False):          
         # Checking for invalid triangle case
        print('No')
        



a=int(input("Enter a number"))
b=int(input("Enter a number"))
flips=0     #counter for flips required
while(a>0 and b>0):
    t1=a&1
    t2=b&1
    if(t1!=t2):
        flips+=1

        a>>=1
        b>>=1

        print("Total flips required is",flips)
