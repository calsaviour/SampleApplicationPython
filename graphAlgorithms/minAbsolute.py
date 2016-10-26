__author__ = 'calvinlowyanming'


def minimize_absolute(L):
    x = 0
    # your code here
    l = len(L)

    if l % 2 != 0:
        index = len(L) / 2
        x = L[index]
    else:
        index = len(L) / 2
        ceiling_v = L[index]
        lower_v = L[index - 1]

        x = (float(ceiling_v) + float(lower_v)) / 2

        print x
    return x


def test():
    L = [6, 5, 4, 5]
    L.sort(reverse=False)
    minimize_absolute(L)
