#!/usr/bin/env python
# coding: utf-8

# ### range() e o conceito onde melhor se aplica, idem ao iterator
# 
#   > **Entendimento:** Imaginando que eu tenha uma sequência de 1 milhão de números, caso eu tenha uma lista para ela, ocuparia muito espaço em memória. Utilizando o range() por exemplo, ele irá retornar o valor apenas no momento em que for chamado. **Validar este conceito e buscar fontes para esclarecer melhor!**

# #### ! No Python, dificilmente precisamos acessar o índice de algo dentro de um for
# ```
# word = 'abracadabra'
# for i in range(len(word)):
#     print(word[i])
# ```
# 
# #### Normalmente terá algo mais alto nível para ser utilizado mais Pythonicamente

# ### Aula:

# In[7]:


nome = 'Henrique'

print(nome, len(nome))

i = 0

for i in range(len(nome)):
    print(nome[i])


# ##### Range:

# In[8]:


range(8)


# In[12]:


r = range(8)
r[0]


# In[13]:


r[-1]


# In[14]:


list(r)


# In[15]:


get_ipython().run_line_magic('pinfo', 'range')


# In[17]:


list(range(1, 20, 3))


# In[18]:


for i in range(8):
    print(i)


# #### Strings são iteráveis:

# In[19]:


for c in nome:
    print(c)


# In[20]:


for i, c in enumerate(nome):
    print(i, c)


# In[23]:


e = enumerate('henrique')


# In[25]:


e


# In[26]:


next(e)


# In[34]:


next(e)


# o for trata o exception

# In[36]:


for i, c in enumerate(nome):
    if c == 'e':
        continue
    print(i, c)


# In[37]:


for i, c in enumerate(nome):
    if c == 'e':
        break
    print(i, c)

