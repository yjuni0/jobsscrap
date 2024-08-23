# BLUEPRINT | DONT EDIT
playing = True

while playing:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input(
        "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
    )
    # /BLUEPRINT

    # 👇🏻 YOUR CODE 👇🏻:
    if operation == "+":
        print(f"Result: {a + b}")
    elif operation == "-":
        print(f"Result: {a - b}")
    elif operation == "*":
        print(f"Result: {a * b}")
    elif operation == "/":
        if b == 0:
            print("Error: 0 cannot be divided")
            continue
        else:
            print(f"Result: {a / b}")
    else:
        if operation.lower() != "exit":
            print("Error: Choose a valid operation")
        else:
            print("bye")
            playing = False

# /YOUR CODE
