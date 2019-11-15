#!/usr/bin/env python
# coding: utf-8

# ## Brincando, testes:

# In[45]:


# Um '=' por linha apenas? -> Posso atribuir mais que um, com mesmo valor
a = b = 2


# In[56]:


# Um '=' por linha apenas? -> O valor deve ser sempre o mesmo? It's sure!!!
[a] = [2] = [3]


# #### Brincando com set, ele não é ordenado, a bagunça abaixo é meramente ilustrativa e não aplicável no mundo real..

# set?
# 
# ```
# 
# Init signature: set(self, /, *args, **kwargs)
# Docstring:     
# set() -> new empty set object
# set(iterable) -> new set object
# 
# Build an unordered collection of unique elements.
# Type:           type
# Subclasses: 
# 
# ```

# In[10]:


# Apesar de funcionar este unpacking, não consigo encontrar alguma aplicação
# que não seja adotar algo como pegar 'aleatóriamente' um valor
# apesar de ele manter a msm (des)ordem após n execuções

s = {'Raul', 'Campinas', 24.1, 24.2}

nome_talvez, cidade_talvez, lat_talvez, lon_talvez = s

print(nome_talvez, cidade_talvez, lat_talvez, lon_talvez)

# s = None # Experimentar limpar para ver se ele mantém a desordem

outro_set = {'Raul', 'Campinas', 24.1, 24.2}
# 'Supondo' que a ordem seja a mesma após execução anterior:
lat_acho, cidade_acho, lon_acho, nome_acho = outro_set
print(nome_acho, cidade_acho, lat_acho, lon_acho)


# In[11]:


# Apesar de funcionar este unpacking, não consigo encontrar alguma aplicação
# que não seja adotar algo como pegar 'aleatóriamente' um valor
# apesar de ele manter a msm (des)ordem após n execuções

s = {'Raul', 'Campinas', 24.1, 24.2}

nome_talvez, cidade_talvez, lat_talvez, lon_talvez = s

print(nome_talvez, cidade_talvez, lat_talvez, lon_talvez)

s = None # Limpando para ver se ele mantém a desordem. Acho que manterá!

outro_set = {'Raul', 'Campinas', 24.1, 24.2}
# 'Supondo' que a ordem seja a mesma após execução anterior:
lat_acho, cidade_acho, lon_acho, nome_acho = outro_set
print(nome_acho, cidade_acho, lat_acho, lon_acho)


# In[21]:


# Ideia de como talvez esteja mantendo a mesma: -> REFUTADA!! Nada a ver com o valor do hash
hash_1 = hash(24.1) #Primeiro
hash_2 = hash('Campinas') #Segundo
hash_3 = hash(24.2) #Terceiro
hash_4 = hash('Raul') #Quarto


print(hash_1) #Primeiro
print(hash_2) #Segundo
print(hash_3) #Terceiro
print(hash_4) #Quarto


print('Hash 2 é maior que o hash 1? ', hash_2 > hash_1)
print('Hash 3 é maior que o hash 2? ', hash_3 > hash_2)
print('Hash 4 é maior que o hash 3? ', hash_4 > hash_3)
print('Hash 4 é maior que o hash 1? ', hash_4 > hash_1)


# In[22]:


s = {'Raul', 'Campinas', 24.1, 24.2}

for e in s:
    print(e)


# In[33]:


# Um erro engraçado -> Na verdade todos os elementos da estrutra terão que ser iteráveis. Como no exemplo, foi uma 
# tupla de tuplas, funcionou.
s = {'Raul', 'Campinas', 24.1, 24.2}

for a, b, c, d in s:
    print(a, b, c, d)


# In[31]:


# Será que com a outra estrutra irá ter o mesmo?
table = ('Henrique', 'Niterói', 22.9, 43.1)

for nome, *_ in table:
    print(nome, _)


# In[37]:


### Isto mostra que atribuição 'pura' é diferente do caso de fazê-lo no for
row = ('Raul', 'Campinas', 22.9, 43.1)

name, city, lat, lon = row
print(name, city, lat, lon)

name, *_ = row
print(name, _)

# Gera erro
for name, *_ in row:
    print(name, _)


# In[39]:


### Talvez esta 'gambi' resolva -> Funcionou
row = ('Raul', 'Campinas', 22.9, 43.1)

name, city, lat, lon = row
print(name, city, lat, lon)

name, *_ = row
print(name, _)

# Atribuir a uma lista ou outra estrutura externa
for name, *_ in [row]:
    print(name, _)


# 
# ---
# 
# 
# ## Códigos feitos seguindo fielmente a aula:

# In[7]:


row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    nome, cidade, lat, long = t[0], t[1], t[2], t[3]
    print(nome, cidade, lat, long)
    
if __name__ == '__main__'    :
    f(row)


# In[8]:


row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    nome, cidade, lat, long = t
    print(nome, cidade, lat, long)
    
if __name__ == '__main__'    :
    f(row)


# In[9]:


row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    nome, cidade = t
    print(nome, cidade)
    
if __name__ == '__main__'    :
    f(row)


# In[11]:


row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    nome, cidade = t[0], t[1]
    print(nome, cidade)
    
if __name__ == '__main__'    :
    f(row)


# In[12]:


row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    nome, cidade = t[:2]
    print(nome, cidade)
    
if __name__ == '__main__'    :
    f(row)


# In[14]:


row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    nome, long = t[0], t[3]
    print(nome, long)
    
if __name__ == '__main__'    :
    f(row)


# In[15]:


row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    nome, long = t[0], t[-1]
    print(nome, long)
    
if __name__ == '__main__'    :
    f(row)


# In[20]:


# Underscore para nomes de variáveis que serão descartadas
row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    nome, _, _, long = t
    print(nome, long, _) # Underscore fica com a última atribuição
    
if __name__ == '__main__'    :
    f(row)


# In[22]:


# unpacking pegando o resto
row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    nome, *_, long = t
    print(nome, long, _)
    
if __name__ == '__main__'    :
    f(row)


# In[23]:


# unpacking pegando o resto
row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    nome, *meio, long = t
    print(nome, long, meio)
    
if __name__ == '__main__'    :
    f(row)


# In[24]:


# unpacking pegando o resto
row = 'Henrique', 'Niterói', 22.9, 43.1

def f(t):
    *_, lat, long = t
    print(lat, long, _)
    
if __name__ == '__main__'    :
    f(row)


# #### Table

# In[28]:


# Table
table = (('Henrique', 'Niterói', 22.9, 43.1),
        ('Vinícius', 'Santarém', 22.4, 54.7))

for row in table:
    nome = row[0]
    cidade = row[1]
    lat = row[2]
    long = row[3]
    print(nome, cidade, lat, long)


# In[29]:


# Table
table = (('Henrique', 'Niterói', 22.9, 43.1),
        ('Vinícius', 'Santarém', 22.4, 54.7))

for row in table:
    nome, cidade, lat, long = row
    print(nome, cidade, lat, long)


# In[31]:


# For ixpérto
table = (('Henrique', 'Niterói', 22.9, 43.1),
        ('Vinícius', 'Santarém', 22.4, 54.7))

for nome, cidade, lat, long in table:
    print(nome, cidade, lat, long)


# In[32]:


table = (('Henrique', 'Niterói', 22.9, 43.1),
        ('Vinícius', 'Santarém', 22.4, 54.7))

for nome, *_ in table:
    print(nome, _)

