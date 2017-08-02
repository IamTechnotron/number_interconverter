import math

print("-- WELCOME TO WHOLE-NUMBER SYSTEM CONVERTER --")
print("   ==================================")
print("[Here you can inter-convert any whole-number of base 2,8,10,16]\n")
while True:
    print("+------------------------------+")
    print("| Please choose from the menu  |")
    print("+------------------------------+\n")
    print(" 1. Decimal      ->  Binary")
    print(" 2. Binary       ->  Decimal")
    print(" 3. Decimal      ->  Octal")
    print(" 4. Octal        ->  Decimal")
    print(" 5. Decimal      ->  Hexadecimal")
    print(" 6. Hexadecimal  ->  Decimal")
    print(" 7. Octal        ->  Binary")
    print(" 8. Binary       ->  Octal")
    print(" 9. Octal        ->  Hexadecimal")
    print("10. Hexadecimal  ->  Octal")
    print("11. Binary       ->  Hexadecimal")
    print("12. Hexadecimal  ->  Binary")
    print("13. To Exit")
    choice = int(input("\n>>> "))

    converted_no = 0
    pos = 0
    pos_coef = 1

# Decimal   ->  Binary
    if choice == 1:
        number_in = int(input("\nEnter the Decimal number: "))
        while number_in:
            remainder = number_in % 2
            number_in = int(number_in / 2)
            pos_coef = int(math.pow(10, pos))
            converted_no = converted_no + remainder * pos_coef
            pos = pos + 1

# Binary    ->  Decimal
    elif choice == 2:
        number_in = int(input("\nEnter the Binary number: "))
        while number_in:
            remainder = number_in % 10
            number_in = int(number_in / 10)
            pos_coef = int(math.pow(2, pos))
            converted_no = converted_no + remainder * pos_coef
            pos = pos + 1

# Decimal  ->  Octal
    elif choice == 3:
        number_in = int(input("\nEnter the Decimal number: "))
        while number_in:
            remainder = number_in % 8
            number_in = int(number_in / 8)
            pos_coef = int(math.pow(10, pos))
            converted_no = converted_no + remainder * pos_coef
            pos = pos + 1

# Octal  ->  Decimal
    elif choice == 4:
        number_in = int(input("\nEnter the Octal number: "))
        while number_in:
            remainder = number_in % 10
            number_in = int(number_in / 10)
            pos_coef = int(math.pow(8, pos))
            converted_no = converted_no + remainder * pos_coef
            pos = pos + 1

# Decimal   ->  Hexadecimal
    elif choice == 5:
        number_in = int(input("\nEnter the Decimal number: "))
        converted_no = ''
        while number_in:
            remainder = number_in % 16
            number_in = int(number_in / 16)
            if remainder < 9:
                converted_no = converted_no + str(remainder)
            elif remainder == 10:
                converted_no = converted_no + 'A'
            elif remainder == 11:
                converted_no = converted_no + 'B'
            elif remainder == 12:
                converted_no = converted_no + 'C'
            elif remainder == 13:
                converted_no = converted_no + 'D'
            elif remainder == 14:
                converted_no = converted_no + 'E'
            elif remainder == 15:
                converted_no = converted_no + 'F'
            converted_no = converted_no[::-1]

    elif choice == 6:
        number_in = input("\nEnter the Hexadecimal number: ")
        print("Sorry, Out OF Order")

# Octal  ->  Binary
    elif choice == 7:
        number_in = int(input("\nEnter the Octal number: "))
        while number_in:
            remainder = number_in % 10
            number_in = int(number_in / 10)
            pos_coef = int(math.pow(8, pos))
            converted_no = converted_no + remainder * pos_coef
            pos = pos + 1

        number_in = converted_no
        converted_no = 0
        pos = 0
        pos_coef = 1
        while number_in:
            remainder = number_in % 2
            number_in = int(number_in / 2)
            pos_coef = int(math.pow(10, pos))
            converted_no = converted_no + remainder * pos_coef
            pos = pos + 1

# Binary  ->  Octal
    elif choice == 8:
        number_in = int(input("\nEnter the Binary number: "))
        while number_in:
            remainder = number_in % 10
            number_in = int(number_in / 10)
            pos_coef = int(math.pow(2, pos))
            converted_no = converted_no + remainder * pos_coef
            pos = pos + 1

        number_in = converted_no
        converted_no = 0
        pos = 0
        pos_coef = 1
        while number_in:
            remainder = number_in % 8
            number_in = int(number_in / 8)
            pos_coef = int(math.pow(10, pos))
            converted_no = converted_no + remainder * pos_coef
            pos = pos + 1

# Octal  ->  Hexadecimal
    elif choice == 9:
        number_in = int(input("\nEnter the Octal number: "))
        while number_in:
            remainder = number_in % 10
            number_in = int(number_in / 10)
            pos_coef = int(math.pow(8, pos))
            converted_no = converted_no + remainder * pos_coef
            pos = pos + 1

        number_in = converted_no
        converted_no = ''
        number_in = int(input("\nEnter the Decimal number: "))
        while number_in:
            remainder = number_in % 16
            number_in = int(number_in / 16)
            if remainder < 9:
                converted_no = converted_no + str(remainder)
            elif remainder == 10:
                converted_no = converted_no + 'A'
            elif remainder == 11:
                converted_no = converted_no + 'B'
            elif remainder == 12:
                converted_no = converted_no + 'C'
            elif remainder == 13:
                converted_no = converted_no + 'D'
            elif remainder == 14:
                converted_no = converted_no + 'E'
            elif remainder == 15:
                converted_no = converted_no + 'F'
            converted_no = converted_no[::-1]

    elif choice == 10:
        number_in = input("\nEnter the Hexadecimal number: ")
        print("Sorry, Out OF Order")

# Binary  ->  Hexadecimal
    elif choice == 11:
        number_in = int(input("\nEnter the Binary number: "))
        while number_in:
            remainder = number_in % 10
            number_in = int(number_in / 10)
            pos_coef = int(math.pow(2, pos))
            converted_no = converted_no + remainder * pos_coef
            pos = pos + 1

            number_in = converted_no
            converted_no = ''
            number_in = int(input("\nEnter the Decimal number: "))
            while number_in:
                remainder = number_in % 16
                number_in = int(number_in / 16)
                if remainder < 9:
                    converted_no = converted_no + str(remainder)
                elif remainder == 10:
                    converted_no = converted_no + 'A'
                elif remainder == 11:
                    converted_no = converted_no + 'B'
                elif remainder == 12:
                    converted_no = converted_no + 'C'
                elif remainder == 13:
                    converted_no = converted_no + 'D'
                elif remainder == 14:
                    converted_no = converted_no + 'E'
                elif remainder == 15:
                    converted_no = converted_no + 'F'
                converted_no = converted_no[::-1]

# Hexadecimal  ->  Binary
    elif choice == 12:
        number_in = input("\nEnter the Hexadecimal number: ")
        print("Sorry, Out OF Order")
# EXIT
    elif choice == 13:
        print("\nExiting...")
        break;
 
    else:
        print("ERROR : WRONG INPUT\nPlease choose correctly !")
        break;

    print("converted no :", converted_no)
    
    print("\n---------------------------------------------------------------------------\n")


