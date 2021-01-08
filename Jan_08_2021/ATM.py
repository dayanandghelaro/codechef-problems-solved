inp = input().split()
x = int(inp[0])
y = float(inp[1])
if 0 < x <= 2000 and 0 < y <= 2000:
    if x > y:
        print(y)
    elif x%5 != 0:
        print(y)
    else:
        t = y - x - 0.50
        if t >= 0:
            print(t)
        else:
            print(y)
        
