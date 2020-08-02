def invert_array(A:list, N:int):
    """
    :param A: array for invert
    :return:
    """
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]


def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    invert_array(A1, 5)
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - passed")
        print(A1)
    else:
        print("#test1 - fail")
        print(A1)

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    invert_array(A2, 8)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - passed")
        print(A2)
    else:
        print("#test2 - fail")
        print(A2)

test_invert_array()