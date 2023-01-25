#!/usr/bin/env python
# coding: utf-8

# In[1]:


d={ 
    'key1':'value'
}
d.update({'name':'username'})



for i in d:
    print(d[i])


# In[13]:


l=[]
d={}
for i in range(2):
    d.update({'key1':input(''),'key2':input('')})
    l.append(d)
print(l)

  


# In[21]:


db=[
    {'nithu52@gmail.com':'ansi2'},
    {'ali20@gmail.com':'123'},
    {'harika45@gmail.com':'krishna'},
    {'sadist2@gmail.com':'abc'}
        
]
username=input('enter username:')
password=input('enter password:')

if username and password in db:
    print('valid')
else:
    print('invalid')


# In[23]:


db=[
    {'nithu52@gmail.com':'nithu'},
    {'ali20@gmail.com':'123'},
    {'harika45@gmail.com':'krishna'},
    {'sadist2@gmail.com':'abc'}
        
]
username=input('enter username:')
password=input('enter password:')
temp={username:password}
if temp in db:
    print('valid')
else:
    print('invalid')
    


# In[42]:


# program to add two matrices
a=[[1,2,3],[3,4,5]]
b=[[3,4,5],[5,7,4]]
sum=[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        sum[i][j]=a[i][j]+b[i][j]

for s in sum:
    print(s)


# 

# In[ ]:


#to take a full seperate row
a=input('').split(' ')
a=list(map(int,input('').split(' ')))


# In[43]:


row=3
col=4
new_arr=[]
for i in range(row):
    a=list(map(int,input('enter element:').split(' ')))
    new_arr.append(a)
print(new_arr)


# In[3]:


#program to display 25 fibnocci series
a=0
b=1
i=0
while i<=25:
    print(a)
    t=a+b
    a=b
    b=t
    i+=1
    
    


# In[2]:


#split & join
s='hello@world'
print(s)
res=s.split(' ')
print(res)


# In[3]:


s='hello world'
print(s)
res=s.split(' ')
print(res)
'-'.join(res)


# In[16]:


s='hello world'
print(s.title())       # here it converts the first letter of the words
print(s.capitalize())  # here only the letter of the first word is capitalized
s1='nithu'
s2='NITHU'
print(s1.upper())
print(s2.lower())
s3='HELLO worLD'
res=s3.swapcase()
print(res)
s4='saki2'  # if it contains space it returns false
print(s4.isalpha())


# In[ ]:


#common methods in string and list
isdigit()
isdecimal()
swapcase()


# In[19]:


a='Mr.Nookaiah is'
age=34
b='years old'
print('Mr.Nookaiah is {} years old'.format(age))


# In[29]:


num=10
print('the square of {:10} is {:.6f}'.format(num,num*num))
print(f'the square of {num} is {num*num:.2f}')


# In[3]:


#Exception Handling
a=int(input())
b=int(input())
i=input()
if(i=='+'):
    print(a+b)
elif(i=='-'):
    print(a-b)
elif(i=='*'):
    print(a*b)
elif(i=='/'):
    
    try:
        print(a/b)
    except:
        print('puppy')
else:
    print('no such operator exist')


# In[1]:


try:
    for i in range(5):
        a=int(input())
except:
    print('incorrect')


# In[27]:


def primary(num):
    for i in range(1,num):
        if num%i==0:
            print ("{} is prime".format(num))
            break
    else:
        print('{} is not prime'.format(num))
primary(int(input('enter number:')))


# In[ ]:


#method1
for i in range(1, num+1):#23 iteration
    pass
#method2
for i in range(2, num):#21
    pass
#method3
for i in range(2, num//2):#10
    pass
#method4
for i in range(2, int(num*0.5)+1):#3
    pass


# In[ ]:


#keyword arguments
def add(num1,num2):
    print('num1:',num1)
    print('num2:',num2)
    
    
    #regular functions
    #default val fun
    #keywrd arg fun
    #var len arg
    


# In[28]:


def add(a,b, *abc):
    print(a)
    print(b)
    print(abc)
print(add(10,20,30,40,50))


# In[ ]:




