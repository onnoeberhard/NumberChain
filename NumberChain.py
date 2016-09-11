def getLiteralNumber(n):
    words = {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE',
             10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN',
             17: 'SEVENTEEN', 18: 'EIGHTEEN', 19: 'NINETEEN', 20: 'TWENTY', 30: 'THIRTY', 40: 'FOURTY', 50: 'FIFTY',
             60: 'SIXTY', 70: 'SEVENTY', 80: 'EIGHTY', 90: 'NINETY', 100: 'HUNDRED', 1000: 'THOUSAND',
             1000000: 'MILLION'}
    if n < 20:
        return words[n]
    elif n < 100:
        return words[int(str(n)[:1]) * 10] + \
               (words[int(str(n)[1:])] if int(str(n)[1:]) > 0 else "")
    elif n < 1000:
        return words[int(str(n)[:1])] + words[100] + \
               (words[int(str(n)[1:2]) * 10] if int(str(n)[1:2]) > 0 else "") + \
               (words[int(str(n)[2:])] if int(str(n)[2:]) > 0 else "")
    elif n < 10000:
        return words[int(str(n)[:1])] + words[1000] + \
               (words[int(str(n)[1:2])] + words[100] if int(str(n)[1:2]) > 0 else "") + \
               (words[int(str(n)[2:3]) * 10] if int(str(n)[2:3]) > 0 else "") + \
               (words[int(str(n)[3:])] if int(str(n)[3:]) > 0 else "")
    elif n < 20000:
        return words[int(str(n)[:2])] + words[1000] + \
               (words[int(str(n)[2:3])] + words[100] if int(str(n)[2:3]) > 0 else "") + \
               (words[int(str(n)[3:4]) * 10] if int(str(n)[3:4]) > 0 else "") + \
               (words[int(str(n)[4:])] if int(str(n)[4:]) > 0 else "")
    elif n < 100000:
        return words[int(str(n)[:1]) * 10] + \
               (words[int(str(n)[1:2])] if int(str(n)[1:2]) > 0 else "") + words[1000] + \
               (words[int(str(n)[2:3])] + words[100] if int(str(n)[2:3]) > 0 else "") +\
               (words[int(str(n)[3:4]) * 10] if int(str(n)[3:4]) > 0 else "") + \
               (words[int(str(n)[4:])] if int(str(n)[4:]) > 0 else "")
    elif n < 1000000:
        return words[int(str(n)[:1])] + words[100] + \
               (words[int(str(n)[1:2]) * 10] if int(str(n)[1:2]) > 0 else "") + \
               (words[int(str(n)[2:3])] if int(str(n)[2:3]) > 0 else "") + words[1000] + \
               (words[int(str(n)[3:4])] + words[100] if int(str(n)[3:4]) > 0 else "") + \
               (words[int(str(n)[4:5]) * 10] if int(str(n)[4:5]) > 0 else "") + \
               (words[int(str(n)[5:])] if int(str(n)[5:]) > 0 else "")
    else:
        return words[1] + words[1000000]


for x in range(1, 1000001):
    y = 1
    path = getLiteralNumber(x) + " (" + str(x) + ")"
    while x != 4:
        x = len(getLiteralNumber(x))
        path += ", " + getLiteralNumber(x) + " (" + str(x) + ")"
        y += 1
    if y >= 7:
        print(path)
        break
