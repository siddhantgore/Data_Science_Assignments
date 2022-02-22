#Q6: Find Which line separates oranges and apples

import math
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input strings


def i_am_the_one(red,blue,line):

    for i in red:
        eq=line.replace('x','*'+str(i[0]))
        eq=eq.replace('y','*'+str(i[1]))
        answer=eval(eq)
        if answer>0:
            pass
        else:
            return "NO"
        
    
    for j in blue:
        eq1=line.replace('x','*'+str(j[0]))
        eq1=eq1.replace('y','*'+str(j[1]))
        answer1=eval(eq1)
        if answer1<0:
            pass
        else:
            return "NO"
    return "Yes"

# Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)]
# Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)]
Lines=["1x+1y+0","1x-1y+0","1x+0y-3","0x+1y-0.5"]
Red=[]
Blue=[]

n=int(input("How many points you want to check: "))
print("Enter Red Points")
print()
for i in range(0,n):
    temp=[]
    x=int(input("X cordinate:- "))
    temp.append(x)
    y=int(input("Y cordinate:- "))
    temp.append(y)
    Red.append(temp)

print("Enter Blue Points")
print()
for i in range(0,n):
    temp=[]
    x=int(input("X cordinate:- "))
    temp.append(x)
    y=int(input("Y cordinate:- "))
    temp.append(y)
    Blue.append(temp)




for i in Lines:
    yes_or_no = i_am_the_one(Red, Blue, i)
    print(yes_or_no)