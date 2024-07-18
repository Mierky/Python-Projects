def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    operators = []
    second_operands = []
    dashes = []
    results = []

    for problem in problems:
        if '+' in problem:
            operator = '+'
            num1, num2 = problem.split('+')
        elif '-' in problem:
            operator = '-'
            num1, num2 = problem.split('-')
        else:
            return "Error: Operator must be '+' or '-'."

        num1 = num1.strip()
        num2 = num2.strip()

        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operands.append(num1)
        operators.append(operator)
        second_operands.append(num2)
        dashes.append('-' * (max(len(num1), len(num2)) + 2))

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results.append(result)


    arranged_problems = []
    arranged_problems.append('    '.join(f"{num.rjust(len(dashes[i]))}" for i, num in enumerate(first_operands)))
    arranged_problems.append('    '.join(f"{operators[i]} {num.rjust(len(dashes[i]) - 2)}" for i, num in enumerate(second_operands)))
    arranged_problems.append('    '.join(dashes))

    if show_answers:
        arranged_problems.append('    '.join(f"{result.rjust(len(dashes[i]))}" for i, result in enumerate(results)))

    return '\n'.join(arranged_problems)

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
