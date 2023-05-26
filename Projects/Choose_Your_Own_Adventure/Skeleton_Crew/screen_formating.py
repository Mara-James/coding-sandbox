

'''
## List of steps for formatting function for skeleton crew
[] make a margin spacer variable to add to the line length
[] check length of item to see if its "<=" to line len-> : print item (ends recursive behaviour, use ternary for pythonic code), else: continue with program
    [] check value of string at index of line_length
        
        [] if string at index of line len is NOT empty, then move back one index (possible recussion?) and check if that is a space character, until you find a space character
            [] then once empty character is found, slice(for strings use"[:]") list at nth index of that space.
            [] make 2 empty variables
                to_print=        [] for all characters in first string from characters @0 till @index of empty character
                remaining_str=   [] for @incex of empty character + 1 till length of item               

        [] if string at inex of line_len IS EMPTY : 
            []make 2 empty variables (of the same name)
                to_print=        [] for all characters in first string from characters @0 till @line_len
                remaining_str=   [] for @line_len + 1 till length of item

!check  [] print (to_print)
        [] fortatting(remaining_str, line_len, margin_len)           
'''

text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ultricies sem id lacus vestibulum viverra"
# this function formats all information fed through it to fit nicely within the cli screen size


def formatting(item, line_len, margin_len):
    left_spacer= " " * margin_len
    # print(item[0:(len(item))])





formatting(text,0,0)
































#     raw_item_list= item.split()
#     # item=item
#     line_count=0
#     formatted_list= []
#     new_str=""
#     line_number={}
#     # for word in raw_item_list:
#     #     line_count += len(word)
#     #     if line_count <=45:
#     #         raw_item_list
#     #     elif line_count >=45:

#     # print( line_count)

#     for word in raw_item_list:
#         if (len(word+" ")+ line_count) <= 45:
#             formatted_list.append(word+" ") 
#             line_count += len(word+ " ")
#         # elif line_count >= 45:
            
        
#     for i in formatted_list:
#         new_str += (i+" ")

#     print( line_count)
#     print(formatted_list)
#     print(new_str)
#     print( raw_item_list )
# formatting(text)

