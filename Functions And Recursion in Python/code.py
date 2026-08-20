def sum(a,b):
    return a+b

result = sum(10,40)
print(result)

def avg3(a,b,c):
    print((a+b+c)/3)

avg3(1,2,3)

# practice question
def length_str(str):
    print(len(str))


str=input("enter string ")
length_str(str)

def print_list(list):
    print(list)

list1=[1,2,3,4]
print_list(list1)

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)


n=int(input("enter number "))
print("factorial of number is :- ",fact(n))


def convert(a):
    result = a*90
    print(result)

convert(5)


def show(n):
    if n==0:
        return
    print(n)
    show(n-1)

show(5)