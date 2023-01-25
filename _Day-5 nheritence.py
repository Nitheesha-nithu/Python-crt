#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Single Inheritence
class A:
    name="Jessie"
    age=25
class B(A):
    age=20
obj=B()
print(obj.name)
print(obj.age)


# In[ ]:


class Shopping:
    name="afg"
    branches=""
    floors=0
class Varieties(Shopping):
    name="asd"
class Staff(Shopping):
    name="cbn"
class Manager(Shopping):
    name="dfg"


# In[6]:


class n1:
    def m1(self):
        print("y so sad")
class n2:
    def m1(self):
        print("are u ok")
class D(n1,n2):
    pass
    
obj=D()
obj.m1()


# In[ ]:


class 


# In[ ]:




