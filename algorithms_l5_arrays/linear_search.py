def array_search(A:list, N:int, x:int):
    """
        :param A: array to search
        :param N: 0 to n-1 index
        :param x: index of the element in the array
        :return: x or -1 (if not found)
        if there are several identical elements in the array,
        the first one will be returned
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1 - passed")
    else:
        print("#test1 - fail")
    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test2 - passed")
    else:
        print("#test2 - fail")
    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("#test3 - passed")
    else:
        print("#test3 - fail")


test_array_search()

