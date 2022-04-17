# Question 1
# Write a function to print "hello_USERNAME!"
def hello_name(user_name):    
    print(user_name)
    return hello_name


hello_name("hello_USERNAME!")


# Question 2
# Write a python function, first_odds that print the odd numbers from 1-100 and returns nothing
def first_odds():
    for i in range (1,100,2):
        print(i)

first_odds()

# Question 3 
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    
    max  =  a_list[0]

    for x in a_list:
        if x > max :
            max = x
    return max

a_list =[23, 45 , 2 , 43, 1, 7]
print(max_num_in_list(a_list))