def MaxBilangan (c, a, s, e):
    c = int(c) ; a = int(a) ; s = int(s) ; e = int(e)
    if c > a and c > s and c > e:
        return c
    elif a > c and a > s and a > e:
        return a
    elif s > c and s > a and s > e:
        return s
    else :
        return e

c, a, s, e = map(int,input().split())
hsl = MaxBilangan(c, a, s, e)
print(hsl)