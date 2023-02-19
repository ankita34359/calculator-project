# Process 1: Take input from the user

# Input: number/operand and operator

operand1 = input(" Enter number1:")
operand2 = input("Enter number2:")
operator = input("Enter the operator:")

# # Lets check the nature of operand
# print(type(operand1), type(operand2))

# Changing formate

# Type Conversion: Changing the data type of one variable to another variable.
operand1 = int(operand1)
operand2 = int(operand2)


# # Lets check the nature of operand again
# print(type(operand1), type(operand2))

# Let's check the operator 
if operator == '+':
  result = operand1 + operand2
elif operator == '-':
  result = operand1 - operand2
elif operator == '*':
  result = operand1 * operand2
elif operator == '/':
  result = operand1/ operand2
else:
  print("I don't know the operator" )

# Let's print the result
print(result)



