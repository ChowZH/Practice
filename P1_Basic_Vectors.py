a = [1, 2, 3]
b = [4, 5, 6]

def elementwise_multiplication(a, b):
    assert (len(a) == len(b))
    vec_out = [[]]*len(a)
    for i in range(len(a)):
        vec_out[i] = a[i]*b[i]
    print (vec_out)

def elementwise_addition(a, b):
    assert (len(a) == len(b))
    vec_out = [[]]*len(a)
    for i in range(len(a)):
        vec_out[i] = a[i]+b[i]
    print (vec_out)

def vector_sum (a):
    out = 0
    for i in range(len(a)):
        out += a[i]
    print (out)

def vector_average (a):
    out = 0
    for i in range(len(a)):
        out += a[i]
    out = out/len(a)
    print (out)

elementwise_multiplication (a, b)
elementwise_addition (a, b)
vector_sum(a)
vector_sum(b)
vector_average(a)
vector_average(b)