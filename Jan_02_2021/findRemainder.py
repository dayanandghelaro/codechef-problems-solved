T = eval(input())
if 1<= T <= 1000:
    for t in range(T):
        a, b = input().split(' ')
        a, b = int(a), int(b)
        if 1 <= a <= 10000 and 1 <= b <= 10000:
            print(a%b)
