#Q4: Students marks dashboard
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input examples

# students=['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10'] 
# marks = [45, 78, 12, 14, 48, 43, 47, 98, 35, 80]
students=[]
marks=[]

n=int(input("How may number of recoord you want to insert:- "))
for i in range(0,n):
    name=(input("Enter Student Name:- "))
    students.append(name)
    mark=int(input("Enter Student Marks:- "))
    marks.append(mark)

def display_dash_board(students, marks):
    temp=[]
    temp=marks.copy()
    temp.sort(reverse=True)
    top_5_students=temp[:5]
    temp.sort()
    least_5_students=temp[:5]
    students_within_25_and_75=[]
    for mark in marks:
        if mark>25 and mark<75:
            students_within_25_and_75.append(mark)
            
    return top_5_students, least_5_students, students_within_25_and_75

top_5_students, least_5_students, students_within_25_and_75 = display_dash_board(students, marks)

print("a.")
for ele in top_5_students:
    print(students[marks.index(ele)]+"  "+str(ele))

print("b.")  
for ele in least_5_students:
    print(students[marks.index(ele)]+"  "+str(ele))

print("c.")
students_within_25_and_75.sort()
for ele in students_within_25_and_75:
    print(students[marks.index(ele)]+"  "+str(ele))