dict={
    "name":"parv",
    "age":21,
    "course":"mca"
}
print(dict)
print(type(dict))
print(dict['name'])
dict['age']=34
print(dict["age"])

dict1={
    "name":"parv",
    "score":{
        "math":89,
        "science":67,
        "arts":56
    }
}

print(dict1)
print(dict1["score"])
print(dict1["score"]['math'])

# dictionary methods

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))
dict.update({"name":"daksh"})
print(dict)

# sets

nums={1,2,3,3,3,4,5}
print(nums)
print(type(nums))

nums.add(34)
print(nums)
nums.remove(1)
print(nums)
nums.clear()
print(nums)
nums.add(3)
nums.add(5)
nums.pop()
print(nums)


set1={1,2,3,4,5}
set2={6,7,8,9,1,2,3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))


# practice question
myDict = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}

print(myDict)

subjects = ["python", "java", "C++", "python", "javascript",
            "java", "python", "java", "C++", "C"]

unique_subjects = set(subjects)

print(len(unique_subjects))

# practice question 2
marks = {}

sub1 = input("Enter subject 1: ")
mark1 = int(input("Enter marks: "))
marks[sub1] = mark1

sub2 = input("Enter subject 2: ")
mark2 = int(input("Enter marks: "))
marks[sub2] = mark2

sub3 = input("Enter subject 3: ")
mark3 = int(input("Enter marks: "))
marks[sub3] = mark3

print(marks)

mySet = {9, 9.0}
print(mySet)


