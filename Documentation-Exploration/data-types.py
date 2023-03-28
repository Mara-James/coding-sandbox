print(2+2) #int
print(50- 5*6) #int
print((50-5*6)/4) #float
print(8/5) # division will always return a float
# print(round(_)) results in an error, as _ does not store the last print
# value within ides only in interactive coding within the terminal

test_concatination= 'this is a test of ' 'automatic string concat' "ination to test its " 'capabilities and '"limitations"
limitations_dict= {"this is"" a ""key": ' this is' " a value"}
multi_line_concatination= ("th""is" " is" ' a ' "sloppy multil"
                           'ine' ' concatination'"..."'but'  
                           " it will print as one!")
# this is very helpful for making code more pythonic and aids in keeping to the
# 80-100 character limit to a line of code!
# for reference the below line of code is exactly 80 characters and the line below that is 100.

#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890

# resizing your window to fit this size is a helpful tool to make sure your code is easy to scan for
# errors, bugs and other logical issues.

print (test_concatination)
print(limitations_dict)
print (limitations_dict.keys())
print ( limitations_dict.values())
print (multi_line_concatination)
