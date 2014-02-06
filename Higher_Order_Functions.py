def square(n):
    return n**2

def add(x,y):
    return x+y

def mult(x,y):
    return x*y

def product(n, term):
    """Returns the product of the first n terms in a sequence"""
    if n == 1:
        return term(n)
    else:
        return term(n)*product(n-1, term)

def accumulate(combiner, start, n, term):
    """returns the result of combining the first n terms in a sequence"""
    if n == start:
        return term(n)
    else:
        return combiner(term(n), accumulate(combiner, start, n-1, term))

def summation_using_accumulate(n, term):
    """an implementation of summation using accumulate"""
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """an implementation of product using accumulate"""
    return accumulate(mult, 1, n, term)

def repeated(f, n):
    """Returns the function that computes the nth application of f"""
    if n == 1:
        return f
    else:
        return compose(f, repeated(f, n-1))

def zero(f):
    """Church numeral 0"""
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    return successor(zero)(f)

def two(f):
    return successor(one)(f)

def add_church(n, m):
    """adds church numerals n and m"""
    return lambda f: lambda x: m(f)(n(f)(x))

def church_to_int(n):
    """converts church numeral n to a python integer"""
    def f(x):
        return x+1
    return n(f)(0)

    
    
