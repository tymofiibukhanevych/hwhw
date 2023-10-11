import sympy


def evaluate_expression(expression):
    try:
        result = sympy.sympify(expression)
        return result
    except sympy.SympifyError:
        return None


print("Welcome to the Math Quiz!")


expression = sympy.randcore.nsimplify(sympy.randcore.make_expr(max_depth=2, variables=('x', 'y', 'z')))

print("Solve the following expression:")
print(expression)


user_answer = input("Enter your answer: ")

correct_answer = evaluate_expression(expression)

if correct_answer is None:
    print("Invalid input. Please enter a valid mathematical expression.")
else:
    user_answer = sympy.sympify(user_answer)

    if user_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print("Sorry, your answer is incorrect. The correct answer is:", correct_answer)