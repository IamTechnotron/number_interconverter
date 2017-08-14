from math import pow


def decimal_from_binary_octal(number_in, base):
    number_in = int(number_in)
    converted_no = 0
    pos = 0
    while number_in:
        remainder = number_in % 10
        number_in = int(number_in / 10)
        converted_no = converted_no + remainder * int(pow(base, pos))
        pos = pos + 1
    return converted_no


def decimal_to_binary_octal(number_in, base):
    number_in = int(number_in)
    converted_no = 0
    pos = 0
    while number_in:
        remainder = number_in % base
        number_in = int(number_in / base)
        converted_no = converted_no + remainder * int(pow(10, pos))
        pos = pos + 1
    return converted_no


def binary_to_from_octal(number_in, base_in, base_out):
    number_in = int(number_in)
    temp = decimal_from_binary_octal(number_in, base_in)
    converted_number = decimal_to_binary_octal(temp, base_out)
    return converted_number


def decimal_to_hexa(number_in):
    number_in = int(number_in)
    set_value = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    converted_no = ''
    while number_in:
        remainder = int(number_in % 16)
        number_in = int(number_in / 16)
        if remainder < 9:
            converted_no = converted_no + str(remainder)
        else:
            converted_no = converted_no + set_value[remainder]
    converted_no = converted_no[::-1]
    return converted_no


def decimal_from_hexa(number_in):
    set_value = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    pos = 0
    converted_no = 0
    for element in number_in[::-1]:
        if element in set_value:
            temp = int(set_value[element] * int(pow(16, pos)))
        else:
            temp = int(element) * int(pow(16, pos))
        pos = pos + 1
        converted_no = converted_no + temp
    return converted_no


def binary_octal_to_hex(number_in, base):
    temp = decimal_from_binary_octal(number_in, base)
    converted_no = decimal_to_hexa(temp)
    return converted_no


def binary_octal_from_hex(number_in, base):
    temp = decimal_from_hexa(number_in)
    converted_no = decimal_to_binary_octal(temp, base)
    return converted_no


if __name__ == '__main__':
    print("-- WELCOME TO WHOLE-NUMBER SYSTEM CONVERTER --")
    print("   ========================================")
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

        if choice == 1:
            number = int(input("\nEnter the Decimal number: "))
            convert = decimal_to_binary_octal(number, 2)

        elif choice == 2:
            number = int(input("\nEnter the Binary number: "))
            convert = decimal_from_binary_octal(number, 2)

        elif choice == 3:
            number = int(input("\nEnter the Decimal number: "))
            convert = decimal_to_binary_octal(number, 8)

        elif choice == 4:
            number = int(input("\nEnter the Binary number: "))
            convert = decimal_from_binary_octal(number, 8)

        elif choice == 5:
            number = int(input("\nEnter the Decimal number: "))
            convert = decimal_to_hexa(number)

        elif choice == 6:
            number = input("\nEnter the Hexadecimal number: ")
            convert = decimal_from_hexa(number)

        elif choice == 7:
            number = int(input("\nEnter the Octal number: "))
            convert = binary_to_from_octal(number, 8, 2)

        elif choice == 8:
            number = int(input("\nEnter the Binary number: "))
            convert = binary_to_from_octal(number, 2, 8)

        elif choice == 9:
            number = int(input("\nEnter the Octal number: "))
            convert = binary_octal_to_hex(number, 8)

        elif choice == 10:
            number = input("\nEnter the Hexadecimal number: ")
            convert = binary_octal_from_hex(number, 8)

        elif choice == 11:
            number = int(input("\nEnter the Binary number: "))
            convert = binary_octal_to_hex(number, 2)

        elif choice == 12:
            number = input("\nEnter the Hexadecimal number: ")
            convert = binary_octal_from_hex(number, 2)

        elif choice == 13:
            print("\nExiting...")
            break

        else:
            print("ERROR : WRONG INPUT\nPlease choose correctly from the menu!")
            continue

        print("converted no :", convert)
    print("\n---------------------------------------------------------------------------\n")

