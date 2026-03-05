def add(a, b):
    return a + b

def sub(a,b):
    return a -b

def product(a,b):
    return a *b

def division (a,b):
    if b==0 :
        print("cannot divisible by zeroo")
    else:
         return a/b



# Calculator Program using Functions and User Choice

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def product(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

def calculator():
    try:
        while True:
            print("----- Simple Calculator -----")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5.Exit")

            choice = int(input("Enter your choice (1-5): "))
            
     
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            if choice == 1:
                print("Result:", add(a, b))

            elif choice == 2:
                print("Result:", sub(a, b))

            elif choice == 3:
                print("Result:", product(a, b))

            elif choice == 4:
                print("Result:", division(a, b))
            
            elif choice ==5:
               print("existing program")
               break

            else:
                print("Invalid choice")
    except ValueError as ve:
        print (ve)

