import math


def delta(a, b, c):
    return b**2 - 4*a*c


def bhaskara(a, b, c):
    delta_value = delta(a, b, c)

    if delta_value < 0:
        return "Delta Negativo"
    else:
        x1 = (-b + math.sqrt(delta_value)) / (2*a)
        x2 = (-b - math.sqrt(delta_value)) / (2*a)
        return f"x1={round(x1, 2)}, x2={round(x2, 2)}"


print(bhaskara(7, 3, 4))
# Saída: Delta Negativo

print(bhaskara(1, 5, 2))
# Saída: x1=-0.44, x2=-4.56

print(bhaskara(3, 10, 2))
# Saída: x1=-0.21, x2=-3.12
