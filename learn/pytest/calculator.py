class CalculatorError(Exception):
    pass


class Calculator:
    """An example calculator."""
    def add(self, a, b):
        try:
            return a + b
        except TypeError:
            raise(CalculatorError())

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b
