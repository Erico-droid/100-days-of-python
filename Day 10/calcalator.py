operations = {}

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide

terminate = False
while not terminate:
    num1 = float(input("What's the first number? "))
    num2 = float(input("What's the second number? "))
    for symbol in operations:
        print(symbol)
    operation = input("Which operation do you want to do? ")

    calculation_function = operations[operation]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")

    if input("Do you want to continue? Y/N: ") != "Y":
      terminate = True
  



