#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Find all of the numbers from 1–1000 that are divisible by 8



nums=[i for i in range(1,1001) if(i%8)==0]
print('Result list:',nums)


# In[2]:


# 2. Find all of the numbers from 1–1000 that have a 6 in them



nums=[i for i in range(1,1001) if '6' in str(i)]
print('Result list:',nums)


# In[3]:


# 3. Count the number of spaces in a string (use string above)


string = "Practice Problems to Drill List Comprehension in Your Head."
print('Print Spaces Count:',string.count(' '))


# In[4]:


# 4. Remove all of the vowels in a string (use string above)



string = "Practice Problems to Drill List Comprehension in Your Head."
vowel="aeiouAEIOU"
print("".join([char for char in string if char not in vowel]))


# In[5]:


# 5. Find all of the words in a string that are less than 5 letters (use string above)



string = "Practice Problems to Drill List Comprehension in Your Head."

words=[x for x in string.split(' ')]
new_word=[word for word in words if(len(word)<5)]
print(new_word)


# In[6]:


#6. Use a dictionary comprehension to count the length of each word in a sentence (use string above)


string = "Practice Problems to Drill List Comprehension in Your Head."
li =  string.split(' ')

d={ word: len(word) for word in  li}
print(d)


# In[7]:


# 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any
# single digit besides 1 (2–9)

numbers = [i for i in range(1,1001) if(True) in [True for j in range(2,10) if(i % j == 0)]]
print(numbers)


# In[8]:


# 8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single
# digit any of the numbers is divisible by

numbers = {i:max([j for j in range(1,10) if i % j == 0]) for i in range(1,1001)}
print(numbers)


# In[ ]:




