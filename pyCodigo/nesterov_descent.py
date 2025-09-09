import numpy as np
import math


def numericalGrad(f, x, delta_x):
    # Numerical gradient
    fx = f(x)
    dx = f(x + delta_x)
    return (dx - fx) / delta_x


def nesterovDescent(f, L, dim, xStart=None, numericalGradient=True, delta_x=1e-5, gradient_function=None,
                    epsilon=None):
    """
    A condition is evaluated by the assert function, if it evaluates to 'True' the code keeps working,
    the code raises an 'Assertion Error' exception otherwise.
    
    Format: 
    assert condition, message
    """""

    assert delta_x > 0, "Step must be greater than zero"

    if xStart is None:
        x = np.zeros(dim)
    else:
        x = xStart

    if epsilon is None:
        epsilon = 0.05

    lambda_prev = 0
    lambda_current = 1

    gamma = 1
    y_prev = x
    alpha = 0.05 / (2 * L)

    if numericalGradient:
        gradient = numericalGrad(f, x, delta_x)
    else:
        gradient = gradient_function(x)

    while np.linalg.norm(gradient) >= epsilon:
        y_current = x - alpha * gradient
        x = (1 - gamma) * y_current + gamma * y_prev
        y_prev = y_current
        lambda_tmp = lambda_current
        lambda_current = (1 + math.sqrt(1 + 4*lambda_prev*lambda_prev)) / 2
        lambda_prev = lambda_tmp

        gamma = (1 - lambda_prev) / lambda_current

        if numericalGradient:
            gradient = numericalGrad(f, x, delta_x)
        else:
            gradient = gradient_function(x)

    return x
