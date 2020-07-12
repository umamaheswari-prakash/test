# 1.list comprehension
list =["even" if i%2==0 else "odd"for i in range(5)]
print(list)
#2. student details
students=[['priya','mukii','Dhana','mani'],
['CSE','Civil','ECE','IT'],
[1999,1998,2000,1997]]
student_detail= [[name[i] for name in students] for i in range(4)]
print (student_detail)