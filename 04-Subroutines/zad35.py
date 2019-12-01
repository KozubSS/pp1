def check(n):
    n = str(n)
    if len(n) > 1:
        return check(n[1:]) + int(n[0])
    else:
        return int(n)


print(check(9198007))