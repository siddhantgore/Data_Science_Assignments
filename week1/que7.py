#Q7: Filling the missing values in the specified formate

# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input strings


# you can free to change all these codes/structure
def curve_smoothing(string):
    # your code
    a = S.split(',')
    count = 0
    middle_store = 0
    # left
    for i in range(len(a)):
        if a[i] == '_':
            count = count + 1  # find number of blanks to the left of a number
        else:
            for j in range(i + 1):
                # if there are n blanks to the left of the number speard the number equal over n+1 spaces
                a[j] = str((float(a[i]) / (count + 1)))
            middle_store = i
            middle_store_value = float(a[i])
            break

        # blanks in the middle
    denominator = 1
    flag = 0
    for k in range(middle_store + 1, len(a)):
        if a[k] != '_':
            denominator = (k + 1 - middle_store)
            flag = k
            break
    flag_value = float(a[flag])
    for p in range(middle_store, flag + 1):
        a[p] = str((middle_store_value+flag_value) / denominator)

    # blanks at the right
    last_value = float(a[flag])
    for q in range(flag, len(a)):
        a[q] = str(last_value / (len(a) - flag))

    return a
    return #list of values

S=  "_,_,30,_,_,_,50,_,_"
smoothed_values= curve_smoothing(S)
for ele in smoothed_values:
    print((ele),end=",")