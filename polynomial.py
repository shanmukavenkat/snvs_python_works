def read_polynomial():
    n = int(input())
    polynomial_dict = {}
    for i in range(n):
        power, coefficient = map(int, input().split())
        polynomial_dict[power] = coefficient
    return polynomial_dict
def get_term(coefficient, power):
    coefficient = abs(coefficient)
    if coefficient == 1 and power != 0:
            coefficient = ''
    if power > 1:
        term = "{}x^{}".format(coefficient, power)
    elif power == 1:
        term = "{}x".format(coefficient)
    elif power == 0:
        term = "{}".format(coefficient)
    return term
def get_polynomial_expression_string(polynomial):
    expression = ""
    degree = max(polynomial.keys())
    for power in sorted(polynomial.keys(), reverse=True):
        coefficient = polynomial[power]
        term = get_term(coefficient, power)
        if power == degree:
            if coefficient > 0:
                expression = term
            elif coefficient < 0:
                expression = '-{}'.format(term)
        else:
            if coefficient > 0:
                expression = "{} + {}".format(expression, term)
            elif coefficient < 0:
                expression = "{} - {}".format(expression, term)
    if expression == "":
        expression = "0"
    return expression
def main():
    polynomial = read_polynomial()
    print(get_polynomial_expression_string(polynomial))

main()