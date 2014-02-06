def g(n):
    """Return the value of G(n) (where G(n) = n for n <= 3 and G(n) = G(n-1) + 2*G(n-2) + 3*G(n-3), if n > 3) computed recursively"""
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)


def g_iter(n):
    """Return the value of G(n) computed iteratively"""
    a, b, c, d = 0, 1, 2, 3
    for _ in xrange(n):
        a, b, c, d = b, c, d, d + 2*c + 3*b
    return a

def has_seven(n):
    """Returns True if n has 7 as a digit and False otherwise"""
    if n&10 == 7:
        return True
    elif n%10 == n:
        return False
    else:
        return has_seven(n//10)


def pingpong(n):
    """Returns the nth element of the ping-pong sequence: the sequence that begins by counting up from one and switches direction when the place in the sequence is a multiple of 7 or contains the digit 7"""
    def switch_number(n):
        result = 0
        for i in range(n):
            if i%7 == 0 or has_seven(i):
                result += 1
            return result
        if n == 1:
            return n
        elif switch_number(n)%2 == 0:
            return pingpong(n-1) - 1
        elif switch_number(n)%2 == 1:
            return pingpong(n-1) + 1

        
            
                
    
    
