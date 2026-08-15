count=1
while count<5:
    print("hello")
    count+=1

# practice question

i=1
while i<=100:
    print(i)
    i+=1

while i>0:
    print(i)
    i-=1

# print multiplication table of a number n

n=int(input("enter number "))
while i<=10:
    print(n*i)
    i+=1



numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in numbers:
    print(num)

x = int(input("Enter number: "))

found = False

for num in numbers:
    if num == x:
        found = True
        break

if found:
    print("Number found")
else:
    print("Number not found")


print("print 1 to 5 num :- ")
for i in range(5):
    print(i)

print("print even num till 10")
for i in range(2,10,2):
    print(i)
print("print odd num till 10")
for i in range(1,10,1):
    print(i)

for i in range(10,0,-1):
    print(i)

# practice question

user_number=int(input("enter the number :- "))
sum=0
i=0
while i<=user_number:
    sum+=i
    i+=1

print("sum of n number :- ",sum)
fact=1
user_number2=int(input("enter the number :- "))
for i in range(1,user_number2+1):
    fact*=i

print("factorial of number is :- ",fact)