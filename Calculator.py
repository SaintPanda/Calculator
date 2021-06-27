#!/usr/bin/env python
# coding: utf-8

# In[2]:


# This block take input number(str) and turns them into numbers  

def scan_block(b):
    b = b.split(",")
    new_b =[]
    for x in b:
        if x != ",":
            new_b.append(float(x)) 
    return new_b


# In[3]:


def plus(b):
    
    new_b = scan_block(b)   
    result = 0
    c=0
    
    for x in new_b:
        result += new_b[c]
        c+=1
    print ("\nLocal result: {}".format(result))
            
    return result
        


# In[4]:


def minus(b):
    
    new_b = scan_block(b)
    result = new_b.pop(0)
   
    c=0
    for x in new_b:
        result -= new_b[c]
        c+=1
    print ("\nLocal result: {}".format(result))
        
    return result
        


# In[5]:


def multiplication(b):
    new_b = scan_block(b)
    result = 1
    c=0
    for x in new_b:
        result *= new_b[c]
        c+=1
    print ("\nLocal result: {}".format(result))
    return result
    


# In[6]:


def division(b):
    
    try:
        new_b = scan_block(b)
        result = new_b.pop(0)
        
        c=0
        for x in new_b:
            result /= new_b[c]
            c+=1
        print ("\nLocal result: {}".format(result))
        return result
    
    except ZeroDivisionError:
        print("No divizion zero")


# In[7]:


def persent(b):  
    new_b = scan_block(b)        
    result = new_b.pop(0)
    c=0
    result *= (new_b[c]/100)
        
    print ("\nLocal result: {}".format(result))
    return result


# In[8]:


def deg(b):
    new_b = scan_block(b)
    result = new_b.pop(0)

    c=0
    for x in new_b:
        result **= new_b[c]
        c+=1
    print ("\nLocal result: {}".format(result))
    return result


# In[27]:


# 1. Select a symbol
# 2. Enter numbers separated by commas (any number) like - 50,24,78,35,45 and other

def Start():
    
    while True:
       
        print("""\n\t1 - Plus (+)
        2 - Minus (-)
        3 - Multiplication (*)
        4 - Division (/)
        5 - Percent (%)
        6 - Degree of (cor)
        7 - Quit (q)""")
        
        Q = input("\nSelect a symbol: ")
        
        if Q in ["+","-","*","/","cor","%"]:
            b = input("\nNumber: ")
            if Q == "+":
                plus(b)
            if Q == "-":
                minus(b)
            elif Q =="*":
                multiplication(b)
            elif Q == "/":
                division(b)
            elif Q == "%":
                persent(b)
            elif Q == "cor":
                deg(b)
                
        elif Q == "q":
                break
           
        else: 
            print("\nBroken choice.")
        
    
    


# In[ ]:


if __name__ == "__main__":
    Start()


# In[ ]:




