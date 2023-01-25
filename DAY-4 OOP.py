#!/usr/bin/env python
# coding: utf-8

# In[3]:


l=[0]*5
print(l)


# In[4]:


#XOR OPERATOR ^ (if 2 operands are true it returns false )
5^10


# In[ ]:


#class Student:
    name=""
    roll_num=""
    branch=""
    marks=0
    attendence=""
    is_using_transpport=False
    def view_marks(self):
        pass
    def view_name(self):
        pass
    def update_name(self,new_name):
        pass
    


# In[10]:


class Student:
    student_name=""
    def __init__(self, name):
        print("object created")
        print(name)
        
s1= Student("Nithu")


# In[35]:


class Student:
    student_name=""
    def __init__(self, name):
        self.student_name=name
s1=Student("Nithu")
s2=Student("Harika")
s3=Student("aali")
s3.student_name="alkeya"
print(s1.student_name)
print(s3.student_name)


# In[1]:


class Bank:
    username=""
    acnt_num=0
    branch_name=""
    def __init__(self,x,y,z):
        self.username=x
        self.acnt_num=y
        self.branch_name=z
    def print_datails(self):
        print('username:',x)
        print('acnt_num:',y)
        print('branch_name:',z)
b1=Bank("satya",12345,"kkd")
b2=Bank("nithya",2345,"rjy")
b3=Bank("sneha",3456,"vskpt") 
b3.acnt_num=12345
print(b3.acnt_num)


# In[ ]:





# In[ ]:





# In[ ]:




