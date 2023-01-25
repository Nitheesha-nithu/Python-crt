#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Animals:
    def animals_barks(self):
        print("janver")
class Dog(Animals):
    def dog_barks(self):
        print("Bow Bow")
class Cat(Animals):
    def cat_barks(self):
        print("Meow Meow")
class Fox(Animals):
    def fox_barks(self):
        print("aowww...")
obj=Cat()
obj.animals_barks()

    


# In[6]:


from abc import ABC

class Area(ABC):
    def calculate_area(self):
        pass
class Square(Area):
    def calculate_area(self):
        print("in calculate area")
        
class Triangle(Area):
    pass
obj=Square()1
obj.calculate_area()


# In[ ]:


class 

