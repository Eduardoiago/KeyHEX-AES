from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
from tqdm import tqdm

def encrypt_message(message, password):
    # Derivação da chave
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Padding
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    # Inicialização do vetor de inicialização
    iv = os.urandom(16)

    # Criptografia AES
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Barra de progresso
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
    # Obtenção do salt e IV
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    ct = encrypted_data[32:]

    # Derivação da chave
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Descriptografar
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Barra de progresso
    with tqdm(total=len(ct), desc="Decrypting") as pbar:
        decrypted_data = b""
        chunk_size = 1024
        for i in range(0, len(ct), chunk_size):
            chunk = ct[i:i + chunk_size]
            decrypted_chunk = decryptor.update(chunk)
            decrypted_data += decrypted_chunk
            pbar.update(len(chunk))

        decrypted_data += decryptor.finalize()

    # Remoção do padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()

    return data.decode()

# Menu Variáveis
optionEncrypt = "          1. Encrypt your message in AES"
optionDecrypt = "          2. Decrypt your message in AES"
optionExit = "          3. Exit"
inputOption = "          Choose an option: "
designLine = "==================================================================="
inputMessageEncrypt = "          Type the message: "
inputMessageDecrypt = "          Enter the encrypted message (in hexadecimal): "
passwordInput = "          Enter the password: "

# Menu
def main():
    while True:
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
                        Your message secure with AES encryption  
                    ==============================================           
        """)
        print(optionEncrypt)
        print(optionDecrypt)
        print(optionExit)
        print(" ") 
        
        choice = input(inputOption)
        
        if choice == "1":
            print(" ")
            message = input(inputMessageEncrypt)
            password = input(passwordInput)
            print(" ")
            encrypted_data = encrypt_message(message, password)
            print(" ")
            print(designLine)
            print("Encrypted message:", encrypted_data.hex())
            print(designLine)
        elif choice == "2":
            print(" ")
            encrypted_data = bytes.fromhex(input(inputMessageDecrypt))
            password = input(passwordInput)
            print(" ")
            decrypted_message = decrypt_message(encrypted_data, password)
            print(" ")
            print(designLine)
            print("Decrypted message:", decrypted_message)
            print(designLine)
        elif choice == "3":
            print("Bye!")
            break
        else:
            print(designLine)
            print("Invalid option! Choose a valid option.")
            print(designLine)

if __name__ == "__main__":
    main()
