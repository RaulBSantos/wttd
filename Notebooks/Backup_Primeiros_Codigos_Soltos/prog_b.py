import prog_a
print('Begin', __name__)

print('Define f_b')


def f_b():
    print('Dentro f_b')
    prog_a.f_a()


print('Chama f_b')
f_b()

print('End', __name__)