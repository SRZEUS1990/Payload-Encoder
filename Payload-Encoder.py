import urllib.parse
import html

def url_encoder(data, encoding_level, encode_spaces=True):
    if encode_spaces:
        encoded_data = urllib.parse.quote(data.replace(' ', '<%20>'))
    else:
        encoded_data = urllib.parse.quote(data)
    for _ in range(encoding_level - 1):
        encoded_data = urllib.parse.quote(encoded_data)
    return encoded_data

def hex_encoder(data, encoding_level, encode_spaces=True):
    if encode_spaces:
        encoded_data = ''.join(['%{0:02x}'.format(ord(char)) if char != ' ' else '<%20>' for char in data])
    else:
        encoded_data = ''.join(['%{0:02x}'.format(ord(char)) for char in data])
    for _ in range(encoding_level - 1):
        encoded_data = ''.join(['%{0:02x}'.format(ord(char)) for char in encoded_data])
    return encoded_data

def html_encoder(data, encoding_level, encode_spaces=True):
    if encode_spaces:
        encoded_data = html.escape(data.replace(' ', '<%20>'))
    else:
        encoded_data = html.escape(data)
    for _ in range(encoding_level - 1):
        encoded_data = html.escape(encoded_data)
    return encoded_data

def unicode_encoder(data, encoding_level, encode_spaces=True):
    if encode_spaces:
        encoded_data = ''.join(['\\u{0:04x}'.format(ord(char)) if char != ' ' else '<%20>' for char in data])
    else:
        encoded_data = ''.join(['\\u{0:04x}'.format(ord(char)) for char in data])
    for _ in range(encoding_level - 1):
        encoded_data = ''.join(['\\u{0:04x}'.format(ord(char)) for char in encoded_data])
    return encoded_data

def process_single_data():
    user_input = input("Enter the data to encode: ")
    return [user_input]

def process_list_data():
    file_location = input("Enter the file location with the list of data: ")
    try:
        with open(file_location, 'r') as file:
            data_list = [line.strip() for line in file.readlines()]
        return data_list
    except FileNotFoundError:
        print("File not found. Please check the file location.")
        return None

def create_output_file(encoded_data_list):
    output_file_name = input("Enter the name of the output file: ")
    with open(output_file_name, 'w') as output_file:
        for encoded_data in encoded_data_list:
            output_file.write(f"{encoded_data}\n")
    print(f"Output file '{output_file_name}' created with encoded data.")

def main():
    print("Choose data type:")
    print("1. Single Data")
    print("2. List of Data")
    data_type = int(input())

    if data_type == 1:
        data_list = process_single_data()
    elif data_type == 2:
        data_list = process_list_data()
        if data_list is None:
            return
    else:
        print("Invalid data type selected.")
        return

    print("\nChoose encoding level:")
    print("1. Single Encoding")
    print("2. Double Encoding")
    print("3. Triple Encoding")
    encoding_level = int(input())

    print("\nChoose encoding type:")
    print("1. URL Encoding")
    print("2. HEX Encoding")
    print("3. HTML Encoding")
    print("4. Unicode Encoding")
    encoding_type = int(input())

    print("\nChoose encoding option:")
    print("1. Encode All Characters")
    print("2. Encode Only Spaces")
    print("3. Encode Characters Excluding Spaces")
    encode_option = int(input())

    encode_spaces = True if encode_option == 2 else False

    encoded_data_list = []
    for user_input in data_list:
        if encoding_type == 1:
            result = url_encoder(user_input, encoding_level, encode_spaces)
        elif encoding_type == 2:
            result = hex_encoder(user_input, encoding_level, encode_spaces)
        elif encoding_type == 3:
            result = html_encoder(user_input, encoding_level, encode_spaces)
        elif encoding_type == 4:
            result = unicode_encoder(user_input, encoding_level, encode_spaces)
        else:
            print("Invalid encoding type selected.")
            return

        print(f"\nOriginal data: {user_input}")
        print(f"Encoded data ({['Single', 'Double', 'Triple'][encoding_level-1]} {['URL', 'HEX', 'HTML', 'Unicode'][encoding_type-1]} Encoding): {result}")
        print("\n" + "=" * 40)

        encoded_data_list.append(result)

    if data_type == 2:
        create_output_file(encoded_data_list)

if __name__ == "__main__":
    main()

