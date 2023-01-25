#!/usr/bin/env python
# coding: utf-8

# In[2]:


#square
lst=[1,2,3,4,5]
for i in lst:
    print(i*i)


# In[5]:


# to show the index number
l=[1,2,3,4,5]
k=3
for i in range(0,len(l)):
    if l[i]==k:
        print(i)


# In[7]:


l=[i for i in range(0,10)] #also  we can perform sqr and cube... like l=[i*ior i in range(0,5)]
print(l)


# In[8]:


# list comprehension
l=[num for num in range(0,51) if num%2==0]
print(l)


# In[9]:


l=[num for num in range(1,100)if num%7==0 or num%9==0]
print(l)


# In[10]:


#to print list in reverse order
l=[1,2,3,4,5]
print(l[::-1])


# In[21]:


l=[1,2,3]
print(l)
l.append(9)   #adds element at the end
print(l)
l.insert(3,4)  #index val,ele
print(l)
l.pop()       #by default pop removes last ele
print(l)
l.remove(1)    #removes the ele
print(l)
a=[1,1,1,2,2,4,5,6]
b=[7,8,9]
a.count(1)    #counts the no of occurances of an ele
a.extend(b)  #extend combines two lists
print(a)


# In[24]:


x=[4,8,9,5,2]    # sorts ele in ascending order by default
x.sort()
print(x)
x.sort(reverse=True) # to sort in decending order
print(x)


# In[ ]:




