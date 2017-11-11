
# coding: utf-8

# In[3]:


#include standard modules
import argparse 

import sys
sys.path.append("/Users/elizabeth/Desktop/sorthelper.py")

from sorthelper import sortNumbers

#initialze the parser
parser = argparse.ArgumentParser()
parser.add_argument("a", nargs="*", type = list, help = "Input a list.")

#read arguments from the command line
args = parser.parse_args()

#get the sum
myList = args.a

#Sort the List
sortNumbers(myList)

#output results
print("The sorted list: ", sortNumbers(myList))



# In[ ]:




