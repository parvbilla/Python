f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

f=open("demo.txt","r")
data=f.read(5)
print("5 character read :- ",data)
f.close()

f=open("demo.txt","r")
line1=f.readline()
print("line 1 :- ",line1)
line2 = f.readline()
print("line 2 :- ",line1)
f.close()

# writing mode

f=open("demo.txt","w")
f.write("i want to learn python")
f.close()

f=open("demo.txt","a")
f.write("\ni also want to learn next.js")
f.close()

f=open("demo.txt","r+")
f.write("abc")
f.write("\nthis is new line")
f.seek(0)
print(f.read())
f.close()


with open("demo.txt",'r') as f:
    data=f.read()
    print(data)

with open("demo.txt",'w') as f:
    f.write("demo.txt file how are u ?")


import os

os.remove("demo.txt")

# practice question

f=open("practice.txt",'w')
f.write("hi everyone\nwe are learning file i/o\nusing java\ni like programming in java")

with open("practice.txt","r") as f:
    data=f.read()

new_data = data.replace("java","python")

with open("practice.txt","w") as f:
    f.write(new_data)

with open("practice.txt","r") as f:
    data=f.read()
    print(data)

with open("practice.txt",'r') as f:
    data=f.read()

if 'learning' in data:
    print("Found")
else:
    print("not found")


def check_for_line():
    word='learning'
    line=1
    with open("practice.txt",'r') as f:
        while True:
            data = f.readline()
            if word in data:
                return line
            if data=='':
                return -1
            
            line+=1


print(check_for_line())


with open("number.txt","r") as f:
    data=f.read()
    

numbers = data.split(",")

count=0;

for num in numbers:
    if int(num)%2==0:
        count+=1
    
    
print(count)

