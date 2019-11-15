#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Backup do terminal do IPython -> %hist

def f():
    return 42
print(f())
def f():
    pass
print(f())
# Toda função retorna algo, se não definido, retorna None
def f(a, b, c):
    print(a, b, c)
f('A', 'B', 'C')
# Acima, parâmetros poiscionais
# Abaixo, parâmetros nomeados
f(a='A', b='B', c='C')
# Vantagem é não importar a ordem
# Valores default:
def f(a, b, c='dC'):
    print(a, b, c)
f('A', 'B', 'C')
f('A', 'B')
f(b='B', a='A')
def f(a, b, c='dC', *args):
    print(a, b, c, args)
f('A', 'B', 'C', 'D', 'E', 'F')
# *args -> Tupla com os valores não atribuidos na chamada da funcção
# *args -> Tupla com os valores POSICIONAIS não atribuidos na chamada da funcção
def f(a, b, c='dC', **kwargs):
    print(a, b, c, kwargs)
f(c='C', z='Z', a='A', f='F', b='B')
# Acima, o **kwargs (nome apenas por convencao), vira um dict dos parâmetros NOMEADOS recebidos pela função
# f(c='C', z='Z', f='F', b='B') # Gera um erro
f('A', 'B', c='C', z='Z', f='F')
def f(a, b, c='dC',*args, **kwargs):
    print(a, b, c, args, kwargs)
f('A', 'B', 'C', 'D', 'E', z='Z', w='W')
# args e kwargs é um recurso bom para esculpirmos fluxos de dados no Python
# Há um recurso novo no Py3 que é o 'required keyword-only argument'
def f(a, b, c='dC',*args, x, y, **kwargs):
    print(a, b, c, x, y, args, kwargs)
# f('A', 'B', 'C', 'D', 'E', z='Z', w='W') # Gera um erro
f('A', 'B', 'C', 'D', 'E', x=1, y=2, z='Z', w='W')
def f(a, b, c='dC',*args, x=42, y=51, **kwargs):
    print(a, b, c, x, y, args, kwargs)
f('A', 'B', 'C', 'D', 'E', z='Z', w='W')
f('A', 'B', 'C', 'D', 'E', x=1, y=2, z='Z', w='W')
def filter(**lookups):
    for k, v in lookups.items():
        print(k.split('__'), v)
filter(name__startswith='Hen', age__lt=30, city__endswith='rói')
def f(*args, **kwargs):
    print(args, kwargs)
f('A', 'B', 'C', z='Z', w='W')
t = 'A', 'B', 'C'
d = dict(z='Z', w='W')
print(t, d)
f(t, d)
# args ficou com todos os atributos posicionais
f(t[0], t[1], t[2], z=d['z'], w=d['w'])
# pythonizando o feito acima:
f(*t, **d)
def add(a, b):
    return a + b
add
type(add)
add.__code__
add.__code__.co_argcount
add.__code__.co_code
add.__code__.co_name
add.__code__.co_varnames
import dis
dis.dis(add)
# Carrega a variavel local a, carrega a variável local b, faz binary add, que consome os dois valores da pilha, resultado do binary_add fica no topo da pilha, e retorna o valor que está no topo da pilha
def add(a, b):
    'Soma a com b'
    return a + b
add
add.__doc__
help(add)
def calc(op, a, b):
    return op(a, b)
calc(add, 2, 3)
def mul(a, b):
    return a * b
calc(mul, 2, 3)
# %hist

