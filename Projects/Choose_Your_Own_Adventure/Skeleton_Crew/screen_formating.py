

'''
## List of steps for formatting function for skeleton crew
[] make a margin spacer variable to add to the line_len
[] check length of item to see if its "<=" to line_len-> : print item (ends recursive behaviour, use ternary for pythonic code), else: continue with program
    [] check value of string at index of line_len
            
        [] if string at index of line_len IS EMPTY : 
            []make 2 empty variables (of the same name)
                to_print=        [] for all characters in first string from characters @0 till @line_len
                remaining_str=   [] for @line_len + 1 till length of item
        
        [] if string at index of line len is NOT empty, then move back one index (possible recussion?) and check if that is a space character, until you find a space character
            [] then once empty character is found, slice(for strings use"[:]") list at nth index of that space.
            [] make 2 empty variables
                to_print=        [] for all characters in first string from characters @0 till @index of empty character
                remaining_str=   [] for @incex of empty character + 1 till length of item               

        

!check  [] print (left_spacer +to_print)
        [] fortatting(remaining_str, line_len, margin_len)           
'''

# text="Lorem ipsum dolor sit amet, consectetur adipi scing elit. Vivamus ultricies sem id lacus vestibulum viverra"
# this function formats all information fed through it to fit nicely within the cli screen size 


def formatting(item, line_len, margin_len):
    # make a margin spacer variable
    left_spacer= " " * margin_len
        #check length of item to see if its "<=" to line len
    if len(item)<= line_len :
        print(left_spacer + item) 
    else: 
        #check value of string at index of line_len
        if item[line_len].isspace():
            print(left_spacer +  item[:line_len])
            formatting(
                       item = item[(line_len+1):],
                       line_len = line_len, 
                       margin_len = margin_len
                       )
        else:
            print(left_spacer + item[:(item[:line_len].rfind(" "))])
            formatting(
                       item = item[(item[:line_len].rfind(" ")+1):], 
                       line_len= line_len, 
                       margin_len= margin_len
                       )
            




