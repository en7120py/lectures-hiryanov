def insert_sort(A):
    """
    Sort list A by inserts
    :param A: list
    :return: ordered array
    """
    pass

def choise_sort(A):
    """
    Sort list A by choise method
    :param A: list
    :return: ordered array
    """
    pass

def bubble_sort(A):
    """
    Sort list A by bubble method
    :param A: list
    :return: ordered array
    """
    pass


def test_sort(sort_algorithm):
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print( "ok" if A==A_sorted else "fail")

    print("testcase #2: ", end="")
    A = list(range(10,20)) + list(range(0,10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print( "ok" if A==A_sorted else "fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print( "ok" if A==A_sorted else "fail")


if __name__ == '__main__':
    test_sort(insert_sort())
    test_sort(bubble_sort())
    test_sort(test_sort())
