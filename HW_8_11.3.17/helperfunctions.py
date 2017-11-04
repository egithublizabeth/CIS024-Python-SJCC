
# coding: utf-8

# # Exercise 4 - Creating your own library
# Create a python module helperfunctions.py with the following functions.
# 
# 1) add - returns the sum of two numbers
# 
# 2) diff - returns the difference between two numbers
# 
# 3) product - returns the product of two numbers
# 
# 4) greatest - returns the greatest of two numbers.
# 
# Import this module in your python program and use the functions your created on any two numbers and print the result.
# 
# Note: Upload the helperfunctions.py module to your github folder along with the notebook file. You can also upload helperfunctions.py to Canvas if you are having trouble copying it to Github

# In[3]:


def add(a,b):
    
    return a+b


# In[4]:


def diff(a,b):
    
    return a-b


# In[10]:


def product(a,b):
    
    return a*b


# In[6]:


def greatest(a,b):
    if (a > b):
        largest = a
    if (b > a):
        largest = b
    if ( b == a):
        largest = (a,b)
        
    return largest

