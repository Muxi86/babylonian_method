def main(S, d):
    '''create a babylonian function.
    
    Args:
        S (int): number
        d (int): numnber
        
    Returns:
        float: result
    '''
    a = (S - d**2)/2 * d
    b = a + d
    x = b - a ** 2 / a * b

    return x
S = int(input("S ="))
d = int(input("d ="))
print(main(S, d))