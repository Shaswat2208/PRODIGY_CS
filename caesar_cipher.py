def caesar_cipher(text, shift, mode):
    encrypted_text = []
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            
            new_pos = (ord(char) - start + shift) % 26 + start
            
            new_char = chr(new_pos)
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)


def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (positive integer): "))
    mode = input("Encrypt or Decrypt? (e/d): ").lower()
    
    shift = shift % 26
    
    if mode == 'e':
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print(f"Encrypted message: {encrypted_message}")
    elif mode == 'd':
        decrypted_message = caesar_cipher(message, -shift, 'decrypt')
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid mode. Please enter 'e' for Encrypt or 'd' for Decrypt.")


if __name__ == "__main__":
    main()
