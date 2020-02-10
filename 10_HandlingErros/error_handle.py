# Errors

# 1. Syntax error (compile-time error)
# - when python program cannot interpret your code, since you didn't follow the correct syntax for Python
# - these type of errors you're likely get to get when you make a typo (indentation)
# - Pycharm will show red underline

# 2. Exceptions (run-time error) - crash
# - when unexpected things happen during the execution of a program (run-time)
# - even if your code is syntactically correct
# - there are many different type of Exception in Python, and you can see which exception is 'thrown (raised)'
# in error message --> READ THE ERROR MESSAGE

while True:
    try:
        a = int(input("Enter a number: "))  # when you writhe something else than int, you'll get 'ValuesError'
        b = int(input("Enter a number: "))  # when you writhe something else than int, you'll get error
        c = a / b  # we can get 'Zero division error'
        print(c)
        break
    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Please enter a number!")
    except ZeroDivisionError as e:
        print("Cannot divide by zero")
        print("Please enter a non-zero number!")
    except KeyboardInterrupt:
        print("\nNo input taken.\n")  # ctrl + c (keyboard interrupt)
    except EOFError as e:
        print(f"{e}")  # ctrl + d (end of file char)
    finally:
        print("All Done!!")