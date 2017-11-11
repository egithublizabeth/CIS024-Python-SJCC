
# coding: utf-8

# In[7]:


import argparse 
#include standard modules

#initialze the parser
parser = argparse.ArgumentParser()
parser.add_argument("x", type = int, help = "Pick a number")
parser.add_argument("y", type = int, help = "Pick another number")

#read arguments from the command line
args = parser.parse_args()

#get the sum
n1 = int(args.x)
n2 = int(args.y)
answer = n1 + n2

#output results
print("The sum is: ", answer)


# In[ ]:




