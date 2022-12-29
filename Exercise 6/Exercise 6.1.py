def validate_integer():
    while True:
        try:
            user_input = int(input("Enter an integer value: "))
        except:
            print("Error")
            continue
        else:
            print("Valid input")
            break
        finally:
            print("Try again - enter an integer value only!")

validate_integer()
