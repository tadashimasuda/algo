def GCD(m,n):
    r = m % n
    if r==0:
        return n

    return GCD(n,r)

if __name__ == "__main__":
    m = int(input())
    n = int(input())

    print(GCD(m,n))