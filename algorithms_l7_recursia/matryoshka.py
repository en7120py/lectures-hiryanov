def matryoshka(n):
    if n == 1:
        print("Matreshechka")
    else:
        print("verh matreshki n=", n)
        matryoshka(n-1)
        print("Niz matreshki n=", n)

if __name__ == '__main__':
    matryoshka(5)