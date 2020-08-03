def sieve(N:int,x:int):
    pass
"""
A=[True]*N
A[0]=A[1]=False
for k in range(2,N):
    if A[k]:
        for m in range(2*k,N,k):
            A[m]=False
for k in range(N):
    print(k, "-", "prime" if A[k] else "composite")

"""


def test_sieve():
    n = sieve(10, 8)
    if n == "composite":
        print("#test1 - passed")
    else:
        print("#test1 - fail")
    n = sieve(20, 7)
    if n == "prime":
        print("#test2 - passed")
    else:
        print("#test2 - fail")
    n = sieve(11, 1)
    if n == "composite":
        print("#test2 - passed")
    else:
        print("#test2 - fail")

test_sieve()