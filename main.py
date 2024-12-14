while True:
    temp = input("Enter the temperatur: ")
    temp_unit = input("(C)elcius or (F)ahrenheit: ")

    if temp_unit.upper() == "C":
        temp = round((float(temp) * 9 / 5) + 32, 2)
        print(f"Temperature in Fahrenheit: {temp}°F")

    elif temp_unit.upper() == "F":
        temp = round((float(temp) -32) * 5 / 9, 2)
        print(f"Temperature in Celcius: {temp}°C")

    else:
        print(f"{temp_unit} or {temp} are invalids, Pls try again!")

    Restart_program = input("(R)estart or (Q)uit: ")
    if Restart_program.upper() == "R":
        continue
    elif Restart_program.upper() == "Q":
        break
    else:
        print(f"'{Restart_program}' is invalid...Restart!...")

