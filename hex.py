def hex_to_decimal(hex_address):
    try:
        decimal_number = int(hex_address, 16)
        print(f"The decimal equivalent of {decimal_number} is {decimal_number}")
    except ValueError:
        print("Invalid hexadecimal address")
