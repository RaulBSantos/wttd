#!/usr/bin/env python
# coding: utf-8

# ### Testando: Por que o erro informado é NotImplemented quando iniciado de um int?

# In[1]:


int('1').__add__('1')


# Tentando com str:

# In[2]:


str(1).__add__(1)


# ### Sobrecarga de Operadores
# #### No fundo is all "Sugar, honey, honey." 
# No Python, os operadores entre outros padrões da linguagem são "Açucar sintático" que acessa algum dunder `__add__`, `__getitem__`, etc
obj + valor == obj.__add__(valor)
# In[1]:


'a'.__add__('b')


# In[3]:


int(1).__add__(1)

obj * valor == obj.__mul__(valor)
# In[ ]:





# **Ponto de atenção** - Sintaxe não é permitida, investigar o motivo (conflita com . flutuante? É por ser um valor mutável diferente de str por exemplo?)

# In[2]:


1.__add__(1)


# In[5]:


[1, 2].__add__([3])


# In[6]:


[1, 2].__getitem__(0)


# No Python eu posso definir na minha classe o que o operador '+' irá fazer por exemplo

#  - [ ] Criar uma classe que faça algo diferente com o '+'

# In[7]:


class MeuSomadorBizarro:
    def __add__(self, item):
        pass

