
# coding: utf-8

# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


7**4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[2]:


s = "Hi there Sam!"
s.split()


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[3]:


planet = "Earth"
diameter = 12742
string_in_string = "The diameter of {} is {} Kilometers.".format(planet,diameter)
print(string_in_string)


# ** Given this nested list, use indexing to grab the word "hello" **

# In[4]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[15]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst[3][1][2][0]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[16]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[22]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[23]:


Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[23]:


def domainGet(email):
    return email.split('@')[1]

domainGet('user@domain.com')


# In[26]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[38]:


def findDog(string):
    new_lst=string.split()
    for l in new_lst:
        if(l.capitalize()=='Dog'):
            return True
    else:
        return False
findDog('Is there a dog here?')


# In[39]:


findDog('Is there a Gog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[49]:


def countDog(string):
    new_lst=string.split()
    count=0
    for l in new_lst:
        if(l.lower()=='dog'):
            count+=1
    return count
countDog('This dog runs faster than the other dog dude!')


# In[31]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[34]:


seq = ['soup','dog','salad','cat','great']


# In[95]:


seq = ['soup','dog','salad','cat','great']
list(filter(lambda x:x.startswith('s'),seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[106]:


def caught_speeding(speed, is_birthday):
    if(is_birthday):
        speed=speed-5
    
    if(speed<=60):
        return "No Ticket"
    elif(speed>60 and speed<=80):
        return "Small Ticket"
    elif(speed>=81):
        return "Big Ticket"


# In[107]:


caught_speeding(81,True)


# In[108]:


caught_speeding(81,False)


# # Great job!
