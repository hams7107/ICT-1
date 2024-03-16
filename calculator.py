class Calculator:
    def __init__(self, expression):
        self.expression = expression

    def calculate(self):
        operators = ['+', '-', '*', '/']
        operands = []
        current_operand = ''

        for char in self.expression:
            if char in operators:
                operands.append(int(current_operand))
                operands.append(char)
                current_operand = ''
            else:
                current_operand += char

        operands.append(int(current_operand))

        result = operands[0]
        for i in range(1, len(operands), 2):
            operator = operands[i]
            operand = operands[i + 1]
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                result //= operand

        return result


if __name__ == "__main__":
    expression = input("Enter expression: ")
    calculator = Calculator(expression)
    result = calculator.calculate()
    print("Result:", result)

