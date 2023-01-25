#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#from Daylogin import User
class User:
    full_name=''
    email=''
    __password=''
    mobile_number=''
    def __init__(self,name,email,password):
        self.full_name=name
        self.email=email
        self.__password=password
    def update_name(self,new_name):
        self.full_name=new_name
    def get_name(self):
        return self.full_name
    """setter method for private variable password"""
    def update_password(self, new_password):
        self.__password=new_password
    def update_mobile_number(self, new_number):
        self.mobile_number=new_number
    """getter method for private variable passwor"""
    def get_user_password(self):
        return self.__password


class Login:
    __db=[]
    def __init(self):
        self.print_menu()
    def print_menu(self):
        print("welcome User")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
    def create_user(self,name,email,password):
        new_user=User(name,email,password)
        self.__db.append(new_user)
        print(self.__db)
        return True
    def validate_user(self,email,password):
        temp=self.__db.copy()
        for user_obj in temp:
            if email == user_obj.email:
                if password == user_obj.get_user_password():
                    return "Login successful"
                else:
                    return "login failed:password is incorrect"
            #returns false if email was not found
            return "Login failed:email was not found"
        
obj=Login() 
while True:
        option=input("enter your choice:")
        if option=='1':
            name=input("enter your full_name:")
            email=input("enter email:")
            password=input("create new password:")
            res=obj.create_user(name,email,password)
            if res == True:
                print("User Created Successfully!")
        elif option=='2':
            email=input('enter email:')
            password=input('enter password:')
            if obj.validate_user(email,password):
                print('login is successfull')
            else:
                print('Login is Unsuccessful')
     
        elif option=='3':
            break
        else:
            print("Invalid Input")
        


# In[ ]:





# In[ ]:




