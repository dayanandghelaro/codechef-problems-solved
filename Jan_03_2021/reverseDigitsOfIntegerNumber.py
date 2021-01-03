# cook your dish here
t = eval(input())
if 1<=t<=1000:
    for i in range(t):
        n = eval(input())
        if 1<=n<=1000000:
            snum = list(str(n))
            snum.reverse()
            n = int("".join(snum))
            print(n)
            
