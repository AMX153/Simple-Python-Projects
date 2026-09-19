import math

print("Welcome to the calculator(Test)")

inp = input("Enter (sin or cos or tan): ")
inp2 = int(input("Enter the number: "))

if inp == 'sin':
    try:
        print(f"The answer is: {math.sin(math.radians(inp2))} \n")
    except Exception as e:
        print(f"Error, the error is: {e}.")
    finally:
        print("The program was run(sin).")
        
elif inp == 'cos':
    try:
        print(f"The answer is: {math.cos(math.radians(inp2))} \n")
    except Exception as e2:
        print("Error, the error is: {e2}.")
    finally:
        print("The program was run(cos).")
        
elif inp == 'tan':
    try:
        print(f"The answer is: {math.tan(math.radians(inp2))}. \n")
    except Exception as e3:
        print(f"Error, the error is: {e3}.")
    finally:
        print("The program was run(tan).")
        
else:
    print("Try again :(")