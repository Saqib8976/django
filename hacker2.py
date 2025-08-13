if __name__ == '__main__':
    a = int(input("enter number1:"))
    b = int(input("enter number2:"))

    c = a+b
    d = a-b
    e = a*b
    print(c)
    print(d)
    print(e)


# The provided code stub reads an integer,n, from STDIN. For all non-negative integers i<n , print i square .

if __name__ == '__main__':
    n = int(input())
    for i in range(0, 100):
        if i < n:
            print(i**2)
