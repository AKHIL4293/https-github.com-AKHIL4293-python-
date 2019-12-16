#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Function
def function1():
    print("Hello, Knowledge Shelf")


# In[3]:


# no argument no return type
def add():
    var1 = int (input("enter the value of num1 : "))
    var2 = int (input("enter the value of num2 : "))
    
    var3 = var1+var2
    print("Sum = ", var3)
    


# In[6]:


# with arguments and no return type
def sub(var1, var2):
    var3 = var1- var2
    print("Sub = ", var3)


# In[7]:


# no arguement and with return type 
def multiply():
    var1 = int (input("enter the value of num1 : "))
    var2 = int (input("enter the value of num2 : "))
    
    var3 = var1*var2
    
    return var3


# In[9]:


# with argument and return type
def div(var1,var2):
    var3 = var1/var2
    return var3


# In[ ]:




