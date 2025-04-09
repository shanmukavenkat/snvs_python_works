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
        expression = 0
    return expression
def get_coefficient(polynomial, power):
    try:
        return polynomial[power]
    except KeyError:
        return 0

def add(p1, p2):
    result = dict()
    for power in (set(p1.keys()) | set(p2.keys())):
        result[power] = get_coefficient(p1, power) + get_coefficient(p2, power)
    return result
def main():
    p1 = read_polynomial()
    p2 = read_polynomial()
    result = add(p1, p2)
    print(get_polynomial_expression_string(result))

main()