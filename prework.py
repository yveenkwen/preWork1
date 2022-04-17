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