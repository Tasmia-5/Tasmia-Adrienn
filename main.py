# Tasmia Any
def pass_encoder(password):
    if password.isdigit() and len(password) == 8:
        encoded_password = ''.join(str((int(char) + 3) % 10) for char in password)
        return encoded_password
    else:
        print("Error: Password should be 8 digits long and contain only integers.")
        return None

def pass_decoder(encoded_password):
    decoded_pass = ""
    pass_list = list(encoded_password)
    for char in pass_list:
        decoded_pass_digit = int(char) - 3
        decoded_pass_digit = str(decoded_pass_digit)
        decoded_pass += decoded_pass_digit
    return decoded_pass


if __name__ == "__main__":
    encoded_password_attempt = ""
    running = True
    while running:

        # Menu
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("\nPlease enter an option: "))

        if option == 1:
            pass_entry = input("Please enter your password to encode: ")
            encoded_password_attempt = pass_encoder(pass_entry)
            if encoded_password_attempt:
                print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {encoded_password_attempt}, and the original password is {pass_decoder(encoded_password_attempt)}")
        elif option == 3:
            running = False
