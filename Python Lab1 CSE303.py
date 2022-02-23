#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Given two integer numbers, write a Python program to return their product. If the product is greater
# than 1000, then return their sum. Read inputs from the user.


def choice(a,b):
    product=a*b
    if(product>1000):
        return (a+b)
    return product

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
print('Result:',choice(a,b))


# In[2]:


#2. Write a Python program to find the area and perimeter of a circle. Read inputs from the user.
import math
def area(r):
    return math.pi*(r**2)

def perimeter(r):
    return 2*math.pi*r

r=float(input("Enter Radius:"))

print('Area:',round(area(r),2))
print('Perimeter:',round(perimeter(r),2))


# In[3]:


# 3. Write a Python program to calculate the compound interest based on the given formula. Read inputs
# from the user.
# A = P * (1 + R/100)^T

#  where P is the principle amount, R is the interest rate and T is time (in years).

# Define a function named as compound_interest_<your-student-id> in your program.

import math
def compound_interest_2018360081(p,r,t):
    return p*(math.pow((1+r/100),t))

p = float(input("Enter Principle: "))
r= float(input("Enter Interest rate: ")) 
t= int(input("Enter time in years: "))
   
print('Result: {:.2f}'.format(compound_interest_2018360081(p,r,t)))


# In[5]:


# 4.Given a positive integer N (read from the user), write a Python program to calculate the value of the
# following series.
#   1^2+2^2+3^2+...+N^2
#sol: 1^2+2^2+3^2+...+N^2=n(n+1)(2n+1)/6

n=int(input('Enter positive integer:'))
result=int((n*(n+1)*(2*n+1))/6)
print("Result:",result)


# In[6]:


# 5.Given a positive integer N (read from the user), write a Python program to check if the number is
# prime or not. Define a function named as prime_find_<your-student-id> in your program.


def prime_find_2018360081(n):
    prime = [True for i in range(n+100)]
    p=2
    for p in range(p, n, p*p): # for (int p = 2; p * p <= n; p++) ->c++
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
  
    print('Number is prime')if(prime[n]) else print('Number is not prime')
 
 
n=int(input('Integer type input:')) 
prime_find_2018360081(n)      


# In[7]:


# 6. Given a positive integer n (read from the user), write a Python program to find the n-th Fibonacci
# number based on the following assumptions.
# Fn = Fn-1 + Fn-2 where F0 = 0 and F1 = 1

def fib(n):
    if(n<=1):
         return n 
    else:
        return fib(n-1)+fib(n-2)
    
n=int(input('Integer type input:')) 
print(str(n)+'th fibonaci number:',fib(n))


# In[8]:


# 7. Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
# the list. Do not use any built-in function.
s="10,20,30,40,50"
li=[int(x) for x in s.split(',')]
sum=0
for i in range(len(li)):
    sum+=li[i]
print("List Sum:",sum)


# In[9]:


# 8. Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
# the even-indexed elements in the list.

s="10,20,30,40,50"
li=[int(x) for x in s.split(',')]
sum=0
for i in range(len(li)):
    if(i%2==0):
        sum+=li[i]
print("List Sum:",sum)   


# In[10]:


# 9. Given a list of numbers (hardcoded in the program), write a Python program to find the largest and
# smallest element of the list. Define two functions largest_number_<your-student-id> and
# smallest_number_<your-student-id> in your program. Do not use any built-in function.


import sys

def largest_number_2018360081(li):
    min=-sys.maxsize - 1
    for i in range(len(li)):
         if(min<li[i]):
             min=li[i]           
    return min     
     
def smallest_number_2018360081(li):
    max= sys.maxsize
    for i in range(len(li)):
         if(max>li[i]):
             max=li[i]           
    return max       
     
s="10,20,30,40,50,1,15,-5,100,66,7"
li=[int(x) for x in s.split(',')]     
print('Largest Element:',largest_number_2018360081(li))
print('Smallest Element:',smallest_number_2018360081(li))


# In[11]:


# 10. Given a list of numbers (hardcoded in the program), write a Python program to find the second
# largest element of the list.

s="10,20,30,40,50,1,15,-5,100,66,7"
li=[int(x) for x in s.split(',')]     
li.sort()
print("Second largest element:{}".format(li[len(li)-2]))


# In[12]:


# 11. Given a string, display only those characters which are present at an even index number. Read inputs
# from the user.

s=input('Input a string:')
rs=''

for x in range(len(s)):
     if((x+1)%2==0):
         rs=rs+str(s[x])
print('Result:',rs)     


# In[13]:


# 12. Given a string and an integer number n, remove characters from a string starting from zero up to n
# and return a new string. N must be less than the length of the string. Read inputs from the user. Do
# not use any built-in function.

s = input("Enter String: ")
n = int(input("Enter a number : "))
cnt = 0
for element in s:
        cnt = cnt + 1
      
ns = ""           
for i in range(n,cnt):
    ns = ns+s[i]
    
print(f'New String : {ns}')


# In[14]:


# 13. Given a string, find the count of the substring “CSE303” appeared in the given string. Do not use any
# built-in function.


s='HELLOFROMCSE303ADDNEWCOURSECSE303eeeeCSE303'
inc=1
cnt=0
for i in range(0,len(s),inc):
    if(s[i]=='C' and s[i+1]=='S'and s[i+2]=='E'and s[i+3]=='3'and s[i+4]=='0'and s[i+5]=='3'):
        inc=inc+5
        cnt=cnt+1
    else:
        inc=inc+1    
        
print('Total substring of CSE303:',cnt) 


# In[15]:


# 14. Given a string, write a python program to check if it is palindrome or not. Define a function named
# palindrome_checker_<your-student-id> in your program.

def palindrome_checker_2018360081(li,s):
    li.reverse()
    flag=0
    for x in range(len(li)):
        if(li[x]!=s[x]):
            flag=1
    return flag        
    
s='redivider'
li=[s[x] for x in range(len(s))]
result=palindrome_checker_2018360081(li,s)
print("{} is Palindrome".format(s))if(result==0) else print("{} is not Palindrome".format(s))


# In[16]:


# 15. Given a two list of numbers (hardcoded in the program), create a new list such that new list should
# contain only odd numbers from the first list and even numbers from the second list.

s1="11,20,33,40,55,1,15,5,100,66,7"
s2="15,2,33,88,65,3,25,57,100,76,9"
li1=[int(x) for x in s1.split(',')]
li2=[int(x) for x in s2.split(',')]
li=[]
for i in range(len(li1)): 
     if(li1[i]%2!=0):
         li.append(li1[i])
    
for i in range(len(li2)): 
     if(li2[i]%2==0):
         li.append(li2[i])
         
li.sort()
print('New list:',li)       


# In[ ]:




