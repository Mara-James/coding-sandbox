#this is a list of python drills
import ipdb

### this is a breif python drill designed to use random
'''
import random

def coin_flip():
    toss= random.randint(0,1)
    if toss == 1:
        print("Heads")
    elif toss == 0:
        print("Tails")
    

coin_flip()

'''

### This is a code drill using random to randomize a choice without using random choice
'''
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

def who_pays():
    choice= random.randint(0,(len(names)))
    print( f'{(names[choice])} is going to buy the meal today!')

who_pays()



'''

### Practice with using for loops and complex index find and replace

'''         
row1 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row3 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row4 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row5 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row6 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row7 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row8 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row9 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]

# row1 = ["C","O","T"]
# row2 = ["P","Y","L"]
# row3 = ["M","S","A"]


map = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

print(f"\n{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}\n")

position = input("Where do you want to put the treasure? ")

def bury():
    cordinates=[int(i)for i in str(position)]
    column= cordinates[0]
    row= cordinates [1]
    
    called_row=map[(row - 1)] 
    called_row[(column - 1)]="X"

    # print (cordinates)
    # print (type(column), column)
    # print (type(row), row)
    # print (called_row)
    
bury()

print(f"\n{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}\n")

'''

#drill to find the average of a list using a for loop without using sum or len
'''
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
print(student_heights)  

sum_of_heights= 0
for value in student_heights:
  sum_of_heights+=value

print (f"Sum of Heights = {sum_of_heights}")

num_of_students=0
for student in student_heights:
  num_of_students+=1

print(f"number of students = {num_of_students}")

averaged_height= round(sum_of_heights/num_of_students)

print (averaged_height)
'''


# drill to find the highest number out of a list of numbers using for loop
'''
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0

for value in student_scores:
  if value > highest_score:
    highest_score= value

print(f'The highest score in the class is: {highest_score}')
'''


# drill to find the sum of all numbers at a set distance from each other using for loop
'''
all_even= [0]
for num in range(0,101,2):
  all_even.append(num)


print (sum(all_even))
'''

# drill to use a for loop to return numbers within a range, with different effects based on met and unmet criteria
'''
for i in range(1,101):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 ==0 :
        print ("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''

