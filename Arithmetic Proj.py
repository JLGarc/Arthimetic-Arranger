def arithmetic_arranger(Equations):
    Length= len(Equations)
    No_of_Dig = 0
    # Checks if we have too many Problems (only up to 5)
    if Length > 5:
        print("Too many Problems")
        quit()
    # Checks for any invalid entries
    for EQ in Equations:
        try:
            parts = EQ.split()
            num1 = int(parts[0])
            num2 = int(parts[2])
        except:
            print("Invalid Entries")
            quit()
        if parts[1] != "+" and parts[1] != "-":
            print("Invalid Operator")
            quit()

    # Finds the largest number of digits for formatting purposes
    for EQ in Equations:
        parts = EQ.split()
        if len(parts[0]) > (len(parts[2]) + 2):
            digits = len(parts[0])
        else:
            digits = (len(parts[2]) + 2)
        if digits > No_of_Dig:
            No_of_Dig = digits
        else:
            No_of_Dig = No_of_Dig
    # Prints the first line
    for EQ in Equations:
        parts = EQ.split()
        i = No_of_Dig - len(parts[0])+3
        while i > 0:
            print(" ", end="")
            i = i -1
        print(parts[0],"     ",end="")
    print("")
    # Prints the second line witht the operator
    for EQ in Equations:
        parts = EQ.split()
        i = No_of_Dig - len(parts[2])
        while i > 0:
            print(" ", end="")
            i = i - 1

        print(parts[1],"", parts[2], "     ",end="")
    print("")
    # Prints dashes for formatting
    for EQ in Equations:
        i = No_of_Dig + 3
        print(" ", end="")
        while i > 0:
            print("-", end="")
            i = i - 1
        print("     ",end ="")
    print("")

    # Prints Answers
    for EQ in Equations:
        parts = EQ.split()
        if parts[1] =="+":
            ans = int(parts[0])+ int(parts[2])
        elif parts[1] =="-":
            ans = int(parts[0]) - int(parts[2])
        else:
            print("Invalid Operator")
            quit()
        i = No_of_Dig - len(str(ans))
        while i > 0:
            print(" ", end="")
            i = i - 1

        print("  ", str(ans),"     ", end = "")



arithmetic_arranger([ "1 + 22", "355 + 12", "22 - 15", "132 + 1"
                      "1 + 23", "4 + 1"])