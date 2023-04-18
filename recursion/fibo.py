def fibo(n, s):
    print("n=", n, s)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1, "f") + fibo(n - 2, "l")


if __name__ == "__main__":
    print(fibo(6, None))
