# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # TO DO ... 
    value = 0
    power = 0
    for number in poly:
        value += number*((x)**power)
        power += 1
    return value

# print evaluate_poly((0.0, 0.0, 5.0, 9.3, 7.0), -13)


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # TO DO ... 
    new_poly = ()
    count = 0
    for number in poly:
        if count is 0:
            count += 1
            continue
        if number is 0.0:
            new_poly += (0.0,)
        else:
            new_poly += (number*count,)
        count += 1
    return new_poly

print compute_deriv((-13.39, 0.0, 17.5, 3.0, 1.0))


def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # TO DO ...
    guess = x_0
    iteration = 0
    while True:
        iteration += 1
        test_root = evaluate_poly(poly, guess)
        poly_derivative = compute_deriv(poly)
        if abs(test_root) < epsilon:
            return (format(test_root, '.10f'), iteration)
        else:
            guess = guess - test_root / evaluate_poly(poly_derivative, guess)

print compute_root((-13.39, 0.0, 17.5, 3.0, 1.0), 0.1, .0001)
