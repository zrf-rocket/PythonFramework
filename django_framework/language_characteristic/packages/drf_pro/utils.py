def select_case():
    calculate = {
        "+": lambda num1, num2: num1 + num2,
        "-": lambda num1, num2: num1 - num2,
        "*": lambda num1, num2: num1 * num2,
        "/": lambda num1, num2: num1 / num2,
        "//": lambda num1, num2: num1 // num2,
        "%": lambda num1, num2: num1 % num2,
    }
    return calculate