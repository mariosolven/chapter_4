# Python program to swap positions between a given list.

## Declaring function with our three variables.
def swap(name_list, first_pos, last_pos): 
    name_list[first_pos],name_list[last_pos] = name_list[last_pos],name_list[first_pos]  ### Swapping our first and last values from our list.
    return name_list
   
name_list = ['Mario', 'Ventura', 'Solórzano'] ### Declaring my values from the list.
first_pos, last_pos  = 1, 3 ### Declaring their positions from my list that each variable has.
print(swap(name_list, first_pos-1, last_pos-1))  ### Printing results.