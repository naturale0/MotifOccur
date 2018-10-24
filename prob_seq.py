import operator as op
import matplotlib.pyplot as plt
from functools import reduce
from math import isinf


def ncr(n, r):
    """
    Combinatorial function written in pure python
    """
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom
    

def p_(n=52, k=7, plot=False):
    """
    prob of the event that at least one 7mer occurs
    """
    answer = 0.
    for i in range(1, n//k+1):
        prob = ncr(n-(k-1)*i, i) * 4.**(-k*i)
        
        if i % 2 == 1:
            answer += prob
        else:
            answer -= prob
    return answer
    

if __name__ == "__main__":
    x = range(500)
    y3 = [p_(n, 3) for n in x]
    y4 = [p_(n, 4) for n in x]
    y7 = [p_(n, 7) for n in x]

    plt.plot(x, y3, label='3nt')
    plt.plot(x, y4, label='4nt')
    plt.plot(x, y7, label='7nt')
    plt.xlabel('length of random sequence')
    plt.ylabel('probability of occurrence')
    plt.legend(loc=2)
    plt.show()
