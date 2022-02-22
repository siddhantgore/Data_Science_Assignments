#Q9: Given two sentances S1, S2

# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input strings

# you can free to change all these codes/structure
def string_features(S1, S2):
    # your code
    b=[]
    c=[]
    a=[]
    S1_temp=S1.split(" ")
    S2_temp=S2.split(" ")
    for ele in S1_temp:
        if ele in S2_temp:
            a.append(ele)
    for ele in S1_temp:
        if ele not in S2_temp:
            b.append(ele)
    for ele in S2_temp:
        if ele not in S1_temp:
            c.append(ele)
    return len(a), b, c

# S1= "the first column F will contain only 5 uniques values"
# S2= "the second column S will contain only 3 uniques values"
S1=input("Enter String1:- ")
S2=input("Enter String2:- ")
a,b,c = string_features(S1, S2)
print(a)
print(b)
print(c)