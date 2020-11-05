def convert(s):
    num = 0
    for i in range(len(s)):
        expo = len(s) - 1 - i
        #num += valueOf(s[i]) * 10**expo
        num = num * 10 + ord(s[i]) - ord('0')

    print(num)


convert("123")