# cook your dish here
t = eval(input())
if 1<=t<=1000:
    for i in range(t):
        sl = input().split(' ')
        l = [int(i) for i in sl]
        if len(l)>=2:
            l.sort()
            print(l[-2])
