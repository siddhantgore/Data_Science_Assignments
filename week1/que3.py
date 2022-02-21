# Q3: Replace the digits in the string with #

import re
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input examples
String="a2b3c4"

def replace_digits(String):
    for word in String:
        if word.isdigit():
            print("#",end="")
      

replace_digits(String)