T = eval(input())
if 1 <= T <= 10:
    for t in range(T):
        n = eval(input())
        if 4 <= n <= 10**5:
            charStr = input()
            chars = "abcdefghijklmnop"
            for i in range(0, n, 4):
                chrs = chars
                encodedChars = charStr[i:i+4]
                for e in encodedChars:
                    if e == '0':
                        chrs = chrs[:len(chrs)//2]
                    else:
                        chrs = chrs[len(chrs)//2 : ]
                print(chrs, end='')
            print()
