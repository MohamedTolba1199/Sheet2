#!/usr/bin/env python
# coding: utf-8

# # Assignment 2 Python
# 

# ## Task1

# In[1]:


options = 'rps'
messages = ["Draw","player A Wins!","player B Wins!"]

def get_XY():
    
    global options,messages
    
    x= input("please Enter the value of A : ").lower().strip()[0]
    y= input("please Enter the value of B : ").lower().strip()[0]
    
    assert x in options and y in options , "invalid arguments!"
    return x,y

def logic(x,y):
    global options,messages
    i=options.index(x)
    j=options.index(y)
    d=abs(i-j)
    
    if d>0:
        if d>1:
            k=2 if i>j else 1
        else:
            k=1 if i>j else 2 
    else:
        k=0
    return messages[k]

def run():
    
    while True:
        try:
            x,y = get_XY()
            break
        except AssertionError:
            print("Invalid Argument!")
            continue 
    messages = logic(x,y) 
    print(messages)
run()    


# ## Task2

# In[12]:


#Opp = ["addition","subtraction","division","multipy"]
x=int(input("please Enter the first number : "))
y=int(input("please Enter the second number : "))

def Add(x,y):
    add=x+y
    return x+y
    
def Sub(x,y):
    sub=x-y
    return x-y
    
def Div(x,y):
    div=x/y
    return x/y
    
def Mul(x,y):
    mul=x*y
    return x*y
     
  
    
Opp =input("PLZ Enter the operation :\n")

if Opp=="addition" :
    print(Add(x,y))
elif Opp=="subtraction" :    
    print(Sub(x,y))
elif Opp== "division" :
    print(Div(x,y))
elif  Opp== "multipy" :
    print(Mul(x,y)) 
else:
    print("Error")
    
    


# ## The Factorial Number
# 

# In[7]:


def fac(n):
    if n==1 or n==0:
        return 1 
    else:
        return n*fac(n-1)
print(fac(10))    
print(fac(1))
print(fac(0))


# ## even or odd number?

# In[9]:


x=int(input("please Enter the first number : "))
if x==0:
    print("Zero")
elif x%2==0:
    print("this number is even ")
else:
    print("this number is odd ")


# In[ ]:




