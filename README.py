def arithmetic_arranger(problems, display_result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        arranged_problems += f"{operand1:>{width}}\n"
        arranged_problems += f"{operator} {operand2:>{width-2}}\n"
        arranged_problems += "-" * width + "\n"

    if display_result:
        results = [str(eval(problem)) for problem in problems]
        width = max(len(result) for result in results) + 2
        arranged_problems += "\n".join(f"{result:>{width}}" for result in results)

    return arranged_problems.rstrip()


# Example usage:
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
result = arithmetic_arranger(problems)
print(result)

result_with_answers = arithmetic_arranger(problems, True)
print(result_with_answers)
