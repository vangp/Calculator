while True:
    print("   Options  ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    #If they pick 1 - 4 I want the calculator to perform the function the user has chosen.
    if (choice >= 1) and choice <= 4:
        print("Enter two numbers: ");
        num1 = int(input());
        num2 = int(input());
        if choice == 1:
            result = num1 + num2;
            print ("Result = ", result);
        elif choice == 2:
            result = num1 - num2;
            print ("Result = ", result);
        elif choice == 3:
            result = num1 * num2;
            print ("Result = ", result);
        elif choice == 4:
            result = num1 / num2;
            print ("Result = ", result);
    elif choice == 5:
        print ("Thank you for using the calculator!")
        exit();
    #If they pick 5 I want it to exit.
    #If they don't enter 1-5 I want to let them know they have entered an incorrect value.
    else:
        print ("Wrong Input!");
        continue
