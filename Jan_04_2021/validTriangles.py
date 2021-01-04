# cook your dish here
t = eval(input())
if 1<=t<=1000:
    for i in range(t):
        a, b, c = input().split()
        a, b, c = int(a), int(b), int(c)
        if 1 <= a <= 180 and 1<=b<=180 and 1<=c<=180:
            if ( (a+b) <= 180) and ( (b+c) <= 180) and ((a+c) <=180) and ((a+b+c) == 180):
                print("YES")
            else:
                print("NO")
