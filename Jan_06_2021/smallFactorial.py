# cook your code here
T = eval(input())
if 1 <= T <= 1000:
    for t in range(T):
        n = eval(input())
        if 0 <= n <= 20:
            if n == 0 or n == 1:
                print(1)
            else:
                fact = 1
                for i in range(n, 1, -1):
                    fact = fact * i
                print(fact)
