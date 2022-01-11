import math

def validate_param():
    attepmts = 3
    while attepmts > 0:
        try:
            print("Enter the variables for an equation of the form :")
            print("ax^2 + bx + c =  0")
            a = int(input("a (not 0) = "))
            b = int(input("b = "))
            c = int(input("c = "))
        except ValueError:
            print("Value is not integer!")
            attepmts -= 1
            continue
        else:
            return a, b, c

def discriminant(a, b, c):
    D = b ** 2 - 4 * a * c
    return D


def roots(D, a, b, c):
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(x1)
        print(x2)
        return x1, x2
    elif D == 0:
        x = -b / (2 * a)
        print("x = %.3f" % x)
        return x
    else:
        print("No roots")

def solv_square(a, b, c) -> roots:
    D = discriminant(a, b, c)
    roots(D, a, b, c)
    print("Discriminant = ", D)

def square_print(a, b, c, roots):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    roots

def main():
    print("Please enter values for equation:")
    valid_params = validate_param()
    a = valid_params[0]
    b = valid_params[1]
    c = valid_params[2]
    solv_square(a, b, c)
    square_print(a, b, c, roots)

if __name__ == "__main__":
    main()