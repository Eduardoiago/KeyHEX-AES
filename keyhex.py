from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
from tqdm import tqdm

# KeyHEX | Console

def encrypt_message(message, password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with tqdm(total=len(padded_data), desc="Encrypting") as pbar:
        encrypted_data = b""
        chunk_size = 1024
        for i in range(0, len(padded_data), chunk_size):
            chunk = padded_data[i:i + chunk_size]
            encrypted_chunk = encryptor.update(chunk)
            encrypted_data += encrypted_chunk
            pbar.update(len(chunk))

        encrypted_data += encryptor.finalize()

    return salt + iv + encrypted_data

def decrypt_message(encrypted_data, password):
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    ct = encrypted_data[32:]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    with tqdm(total=len(ct), desc="Decrypting") as pbar:
        decrypted_data = b""
        chunk_size = 1024
        for i in range(0, len(ct), chunk_size):
            chunk = ct[i:i + chunk_size]
            decrypted_chunk = decryptor.update(chunk)
            decrypted_data += decrypted_chunk
            pbar.update(len(chunk))

        decrypted_data += decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()

    return data.decode()

def info():
    clear_screen()
    print(designLine)
    print("♦  KEYHEX™  ♦")
    print(designLine)
    print("Github: https://github.com/Eduardoiago")
    print("Developed by Eduardo Iago | Version 1.0.0\n")
    print("The tool mission is to transform your message into an AES algorithm with SHA-256 in CFB mode that can only be decrypted with the encrypted code and password.\n")
    print("Before encrypting your messages and links, the tool processes SubBytes, ShiftRows, MixColumns and AddRoundKey. Remember to use strong passwords.\n")
    print("Visit the project documentation (https://github.com/Eduardoiago/KeyHEX-AES) to better understand how keyHEX works.")
    input("\nPress ENTER to return to the Menu.")

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

optionEncrypt = "          1. Encrypt in AES"
optionDecrypt = "          2. Decrypt in AES"
optionExit = "          3. Exit\n"
inputOption = "          Choose an option: "
designLineE = "===== keyHEX ===========================[SHA]256==============="
designLineD = "===== keyHEX ================ Decrypted message ==============="
designLine = "==============================================================="
inputMessageEncrypt = "\n          Type the message: "
inputMessageDecrypt = "          Enter the encrypted message (in hexadecimal): "
passwordInput = "\n          Enter the password: "

def main():
    while True:
        clear_screen()
        print("""       
              
                     ♦  KEYHEX™ version 1.0 ♦
              
                     ██ ▄█▀▓█████▓██   ██▓ ██░ ██ ▓█████ ▒██   ██▒
                     ██▄█▒ ▓█   ▀ ▒██  ██▒▓██░ ██▒▓█   ▀ ▒▒ █ █ ▒░
                    ▓███▄░ ▒███    ▒██ ██░▒██▀▀██░▒███   ░░  █   ░
                    ▓██ █▄ ▒▓█  ▄  ░ ▐██▓░░▓█ ░██ ▒▓█  ▄  ░ █ █ ▒ 
                    ▒██▒ █▄░▒████▒ ░ ██▒▓░░▓█▒░██▓░▒████▒▒██▒ ▒██▒
                    ▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒  ▒ ░░▒░▒░░ ▒░ ░▒▒ ░ ░▓ ░
                    ░ ░▒ ▒░ ░ ░  ░▓██ ░▒░  ▒ ░▒░ ░ ░ ░  ░░░   ░▒ ░
                    ░ ░░ ░    ░   ▒ ▒ ░░   ░  ░░ ░   ░    ░    ░  
                    ░  ░      ░  ░░ ░      ░  ░  ░   ░  ░ ░    ░  
                                  ░ ░                         
                    ==============================================
                           AES Cryptography | SHA-256 in CFB mode  
                    ==============================================           
        """)
        print(optionEncrypt)
        print(optionDecrypt)
        print(optionExit)
        
        choice = input(inputOption)
        
        if choice == "1":
            message = input(inputMessageEncrypt)
            password = input(passwordInput)
            print(" ")
            encrypted_data = encrypt_message(message, password)
            print(" ")
            print(designLineE)
            print(encrypted_data.hex())
            print(designLine)
            input("\nPress ENTER to return to the Menu.")
        elif choice == "2":
            encrypted_data = bytes.fromhex(input(inputMessageDecrypt))
            password = input(passwordInput)
            print(" ")
            decrypted_message = decrypt_message(encrypted_data, password)
            print(" ")
            print(designLineD)
            print(decrypted_message)
            print(designLine)
            input("\nPress ENTER to return to the Menu.")
        elif choice == "3":
            print("\nBye!")
            break
        elif choice == "--info":
            info()
        else:
            print(designLine)
            print("\nInvalid option! Choose a valid option.")
            print(designLine)

if __name__ == "__main__":
    main()
