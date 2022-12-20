def main(S, d):

    a = (S - d**2)/(2 * d)
    b = a + d
    x = b - (a ** 2) / (2 * b)

    return float(x)
S = int(input("S ="))
d = int(input("d ="))
print(main(S, d))