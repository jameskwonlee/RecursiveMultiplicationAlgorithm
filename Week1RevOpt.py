"""
Karatsuba Recursive Multiplication - implemented by JKL for the Stanford Algorithms course

Challenge: Multiply two n digit numbers, one digit at a time using recursive multiplication.

Pseudocode:

Base case:
if n<=2:
Use the star equation, which is: result = 10 ** n * ac + 10 ** (n / 2) * (ad + bc) + bd

Steps for the algorithm for the recursive step:
1. Compute values of a, b, c, and d.
2. Determine term ac by recursively multiplying a and c
3. Determine term ad + bc by recursively multiplying a and d, and b and c, then add them together
4. Determine bd by recursively multiplying b and d
6. Use the star equation on ac, ad, bc, and bd to compute the result

"""


def main():

    # Input numbers
    multiplier = "3141592653589793238462643383279502884197169399375105820974944592"
    multiplicand = "2718281828459045235360287471352662497757247093699959574966967627"

    result = multiply(multiplier, multiplicand)

    print(result)
    return result


def multiply(multiplier, multiplicand):

    # update n value
    n = len(str(multiplier))

    # base case
    if n <= 2:
        a, b = ab_separator(multiplier, n)
        c, d = cd_separator(multiplicand, n)

        ac = int(a) * int(c)
        ad_plus_bc = int(a) * int(d) + int(b) * int(c)
        bd = int(b) * int(d)

        return star_equation(n, ac, ad_plus_bc, bd)

    # separate inputs into halves
    a, b = ab_separator(multiplier, n)
    c, d = cd_separator(multiplicand, n)

    # form separated variables into terms in the star equation
    ac = multiply(a, c)
    ad_plus_bc = multiply(a, d) + multiply(b, c)
    bd = multiply(b, d)

    # use star equation to return a value
    return star_equation(n, ac, ad_plus_bc, bd)


def ab_separator(multiplier, n):
    midpoint = n // 2
    a = multiplier[:midpoint]
    b = multiplier[midpoint:]
    return a, b


def cd_separator(multiplicand, n):
    midpoint = n // 2
    c = multiplicand[:midpoint]
    d = multiplicand[midpoint:]
    return c, d


def star_equation(n, ac, ad_plus_bc, bd):
    result = int(10 ** n * ac + 10 ** (n // 2) * ad_plus_bc + bd)
    return result


if __name__ == '__main__':
    main()