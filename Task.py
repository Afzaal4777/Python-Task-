def add (num1,num2):
   return num1+num2

def sub(num1,num2):
   return num1-num2

def prod(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2 == 0:
        raise ValueError("Division by zero is not allowed")
    return num1/num2
def main():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter the operator")

            if op == "+":
                print(f"{num1}+{num2} = {add(num1, num2)}")
            elif op == "-":
                print(f"{num1}-{num2} = {sub(num1, num2)}")
            elif op == "*":
                print(f"{num1}*{num2} = {prod(num1, num2)}")
            elif op == "/":
                print(f"{num1}/{num2} = {divide(num1, num2)}")
            else:
                print("Invalid operator. Please try again")
        except ValueError as e:
            print(f"Error:{e}")

        cont = input("Do u want to continue? (yes/no): ")
        if cont.lower()!= "yes":
            break
if __name__ == "__main__":
        main()                     