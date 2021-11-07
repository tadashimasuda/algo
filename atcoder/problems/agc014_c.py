def change(A:int,B:int,C:int,cnt:int):

    if A%2==1 or B%2==1 or C%2==1:
        return cnt

    if A==B and A==C:
        if cnt == 0:
            return -1
        return cnt

    return change((B+C)/2,(A+C)/2,(A+B)/2,cnt+1)



if __name__ == "__main__":
    A,B,C =list(map(int,input().split(' ')))

    cnt = 0
    print(change(A,B,C,cnt))


