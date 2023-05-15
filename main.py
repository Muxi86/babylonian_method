def main(S, d):

    a = (S - d**2)/(2 * d)
    b = a + d
    x = b - (a ** 2) / (2 * b)

    return float(x)
print(main(26, 5))