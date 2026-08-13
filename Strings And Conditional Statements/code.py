str1='parv'
print(len(str1))
str2="college"
print(str2)
final_str=str1+" "+str2
print(final_str)
print(str1[0])
print(str1[1:4])
print(str2[:4])
print(str2[:-1])

str3="i am a coder"

print("string functions:- ")
print(str3.endswith("er"))
print(str3.capitalize())
print(str3.replace("i am a code","i am a python coder"))
print(str3.find("am"))
print(str3.count("am"))

# practice question
name=input("enter your name ")
print(len(name))
str4="string"
print(str4.count("$"))

# conditional statement

age=int(input("enter your age :- "))
if(age>18):
    print("you can vote")
elif(age==18):
    print("vote next year")
else:
    print("you cannot vote")


# practice question

num1=int(input("enter the number :- "))
if(num1%2==0):
    print("number is even")
else:
    print("number is odd")

a=int(input("enter the number1 :- "))
b=int(input("enter the number2 :- "))
c=int(input("enter the number3 :- "))

if(a>b and a>c):
    print("a is greatest of 3 num")
elif(b>a and b>c):
    print("b is greatest of 3 num")
else:
    print("c is greatest of 3 num")


num2=int(input("enter the number :- "))
if(num2%7==0):
    print("multiple of 7")
else:
    print("not mutiple of 7")