x = int(input())


if (x < 1):
    print(sum(range(x, 1))+1)
else:
    print(sum(range(1, x+1)))
