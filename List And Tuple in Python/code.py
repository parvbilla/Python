marks=[90,91,95,96,97]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

print(marks[1:4])
print(marks[:3])
print(marks[:-1])

marks.append(100)
print(marks)

marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(0,4)
print(marks)
marks.remove(90)
print(marks)
marks.pop(2)
print(marks)

# tuple

tup=(1,2,3,5,6,7,8)
print(tup)
print(type(tup))
print(tup[0])
# tup[0]=5 not allowed

print(tup.index(1))
print(tup.count(3))

# practice question

movie1=input("enter movie name 1 ")
movie2=input("enter movie name 2 ")
movie3=input("enter movie name 3 ")

movies=[]
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

my_list=[1,2,3,4,5]

if(my_list==my_list[::-1]):
    print("palindrome")
else:
    print("not palindrome")


# practice question part 2

tup_new=('c','d','a','a','b','b','a')
print(tup_new.count('a'))

tuple_new=list(tup_new)
tuple_new.sort()
print(tuple_new)

