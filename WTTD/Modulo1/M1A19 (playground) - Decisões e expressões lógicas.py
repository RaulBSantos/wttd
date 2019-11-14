#!/usr/bin/env python
# coding: utf-8

# In[2]:


'None' and 1


# In[4]:


True and None # Com None ele parece não retornar!!!


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ##### Backup da aula:

# In[8]:


nome = 'henrique'

for c in nome:
#     if c == 'e' or c == 'i' or c == 'u':
# if c in ('e', 'i', 'u'):
    if c in 'aeiou':
        print(c.upper())
    else:
        print(c)
    
    if c == 'q':
        print('@')


# In[9]:


nome = 'henrique'

for c in nome:
    if c in 'aeiou':
        print(c.upper())
    elif c == 'q':
        print('@')
    else:
        print(c)


# In[10]:


True and True


# In[11]:


True and False


# In[12]:


True or True


# In[13]:


True or False


# In[14]:


bool(None)


# In[15]:


bool(False)


# In[16]:


bool(0)


# In[17]:


bool('')


# In[18]:


bool(())


# In[19]:


bool([])


# In[20]:


bool({})


# Expressões True:

# In[21]:


bool(1)


# In[22]:


bool(['abc'])


# Curto Circuito:

# In[23]:


True and 'abc'


# In[24]:


True and []


# In[25]:


[] and True


# In[26]:


1 or []


# In[27]:


1 or indefinido # Notar que não gera erro, nem roda o evaluation


# In[28]:


indefinido


# In[29]:


1 and indefinido


# In[30]:


indefinido = True


# In[31]:


1 and indefinido


# In[ ]:





# In[ ]:





# In[ ]:




