
<img src="/assets/img/title-KeyHex.jpeg" alt="title-keyhex">

> # KEYHEX

#### AES Encryption Python Script

The KeyHEX project is an interactive tool developed in Python that allows users to encrypt and decrypt messages using AES (Advanced Encryption Standard). The tool mission is to transform your message into an AES algorithm with SHA-256 in CFB mode that can only be decrypted with the encrypted code and password. Before encrypting your messages and links, the tool processes SubBytes, ShiftRows, MixColumns and AddRoundKey. Remember to use strong passwords. KeyHEX was an experiment to study AES encryption. 

_GUI development in progress._

## What is Cryptography?

Cryptography is the science of providing security and protection of information. It is used everywhere in our digital world: when you open a Web site, send an email or connect to the WiFi network. 

## AES (_Advanced Encryption Standard_).

<details>
<summary>
    <h3>Advanced Encryption Standard</h3>
</summary><br>

AES is a variant of the Rijndael block cipher developed by two Belgian cryptographers, `Joan Daemen` and `Vincent Rijmen`, who submitted a proposal to NIST during the AES selection process. Rijndael is a family of ciphers with different key and block sizes. For AES, NIST selected three members of the Rijndael family, each with a block size of 128 bits, but three different key lengths: 128, 192 and 256 bits.

AES is a symmetric encryption algorithm, which means that it uses the same key to encrypt and decrypt data. It operates on blocks of data and is designed to be fast and efficient on a wide variety of devices. AES replaced the old DES (Data Encryption Standard) encryption algorithm. 

_AES consists of several steps, including byte substitutions, row permutations, column permutations and key addition, all applied repeatedly in multiple rounds. These complex operations provide a robust security layer against a variety of known cryptographic attacks._

**Visualization of the AES round function**:
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSjoUEnGcbyjc8m8YEsG0uayAtN4KK3DvGQw&usqp=CAU" alt="roundFunction">
</details>

<details>
<summary>
    <h3>Description of the Ciphers</h3>
</summary><br>

AES is based on a design principle known as a substitution–permutation network, and is efficient in both software and hardware. Unlike its predecessor DES, AES does not use a Feistel network. AES is a variant of Rijndael, with a fixed block size of 128 bits, and a key size of 128, 192, or 256 bits. By contrast, Rijndael per se is specified with block and key sizes that may be any multiple of 32 bits, with a minimum of 128 and a maximum of 256 bits. Most AES calculations are done in a particular finite field.

AES operates on a 4 × 4 column-major order array of 16 bytes b0, b1, ..., b15 termed the state.

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSb9gHdsUaRHfPxATzjpYsmT4tHfEjcuc_BU1-oeaWHFqcx5tOeVh9_aBTC&s=10" alt="columnBytes">

The key size used for an AES cipher specifies the number of transformation rounds that convert the input, called the plaintext, into the final output, called the ciphertext. The number of rounds are as follows:

- 10 rounds for 128-bit keys.
- 12 rounds for 192-bit keys.
- 14 rounds for 256-bit keys.

Each round consists of several processing steps, including one that depends on the encryption key itself. A set of reverse rounds are applied to transform ciphertext back into the original plaintext using the same encryption key.
</details>

<details>
<summary>
    <h3>Description of the Algorithm</h3>
</summary><br>    

`KeyExpansion`  – Round keys are derived from the encryption key using AES key planning . AES requires a separate 128 - bit key block round for each round plus one.

**Addition of early round bracket**:

`AddRoundKey`  – each byte of the state is combined with a byte of the round key using xor bitwise operations.

**9, 11 or 13 rounds**:

1. `SubBytes` – a non- linear  replacement step where each byte is replaced by another according to a lookup table.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/AES-SubBytes.svg/1280px-AES-SubBytes.svg.png" alt="SubByts">

2. `ShiftRows` – a transposition step in which the last three lines of the state are cyclically shifted by a certain number of steps.

<img src="https://upload.wikimedia.org/wikipedia/commons/6/66/AES-ShiftRows.svg" alt="ShiftRows">

3. `MixColumns` – a linear mixing operation that operates on the columns of the state, combining the four bytes in each column.

<img src="https://upload.wikimedia.org/wikipedia/commons/7/76/AES-MixColumns.svg" alt="mixcolumns">

4. `AddRoundKey` - In the AddRoundKey step , the subkey is combined with the state. For each round, a subkey is derived from the main key using AES key planning and each subkey is the same size as the state. The subkey is added by matching each state byte with the corresponding byte of the subkey using bitwise XOR .

<img src="https://upload.wikimedia.org/wikipedia/commons/a/ad/AES-AddRoundKey.svg" alt="addKey">

**Final round (making 10, 12 or 14 rounds in total)**:

- SubBytes
- ShiftRows
- AddRoundKey
</details>

<details>
<summary>
    <h3>Calculate SHA-256 Hash</h3>
</summary><br>    
    
|Input|Output      |
|-----|------------| 
|hello|2cf24dba5fb0a30e26e83b2ac5b5e29e1b161e5c1fa7425e79043062938b9824|

_The longer the encrypted message, the longer the hexadecimal code._
</details>

__________________________________________________________

- ## Requirements:

#### Installing Libraries

``` bash
    pip install cryptography 
```
The Python `cryptography` library is a powerful tool for implementing cryptography and security in Python applications. It supports a wide range of cryptographic algorithms, such as AES, RSA, HMAC and many more.

``` bash
    pip install os
```
The `os` library in Python provides an interface for interacting with the underlying operating system. 

``` bash
    pip install tqdm
```
The `tqdm` library was also used to generate a progress bar.
__________________________________________________________

## Functionalities:

1. **Encrypt messages, passwords and personal data**: the user can enter a message and a password to encrypt it.

2. **Decrypt AES message**: the user can enter an encrypted message (in hexadecimal) and a password to decrypt it.

3. It uses the AES algorithm in CFB mode (_Cipher Feedback Mode_) to encrypt the data. It also uses _PBKDF2_ to derive the key from a supplied password.

## Interface console:

<img src="https://i.ibb.co/GtmN7B2/interface-image1.png" alt="interface-image1" border="0">

## Video demo KeyHEX

[![Alt text](https://img.youtube.com/vi/2bGmIa1zv4A/0.jpg)](https://www.youtube.com/watch?v=2bGmIa1zv4A)

## Explained of Code

<details>
    <summary>
        <h3>Libraries</h3>
    </summary>

The libraries needed for encryption and interaction with the operating system are important. This includes the standard encryption backend, padding functions, encryption algorithms (AES), modes of operation (CFB), hashing algorithms (SHA256), a function for deriving keys from a password (PBKDF2HMAC), and a library for generating random numbers.

``` python
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    import os
    from tqdm import tqdm
```
</details>

<details>
    <summary>
        <h3>encrypt_message Function</h3>
    </summary>
    
`Encrypt_message` function: This function takes a message and a password as input and returns the encrypted message. The process is as follows:

- Generates a "salt" value (16 random bytes) to strengthen the password.

- Derives an encryption key from the password using the PBKDF2HMAC function with SHA256.
  
- Adds PKCS7 padding to the message.
Generates a random initialization vector (IV).

- Creates a Cipher object to encrypt the message using AES in CFB mode.
  
- Iterates over the message by encrypting it in 1024-byte chunks and updating a progress bar.
  
- Returns the concatenated salt, IV and encrypted message.
</details>

<details>
    <summary>
        <h3>decrypt_message Function</h3>
    </summary>

`Decrypt_message` function: This function receives the encrypted message and password, and returns the original message. The process is as follows:

- Extracts the salt, IV and encrypted message from the received message.

- Derives the encryption key from the password and salt using PBKDF2HMAC.
  
- Creates a Cipher object to decrypt the message using AES in CFB mode.
  
- Iterates over the encrypted message by decrypting it into 1024-byte chunks and updating a progress bar.
  
- Removes the padding from the decrypted message and returns the original message.
</details>

<details>
    <summary>
        <h3>Notes</h3>
    </summary>

The code uses PBKDF2HMAC to derive the encryption key from the password, which is a best practice to increase security.

PKCS7 padding is used to ensure that the message is of a size compatible with the AES algorithm.

The CFB mode of operation is used for encryption, which is a block mode of operation that makes encryption more efficient for operations on smaller chunks of data.

The use of a random initialization vector (IV) is essential to ensure that messages encrypted with the same key do not generate the same ciphertext.
</details>

## License
 * [MIT](LICENSE)

## Technologies used:

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)&nbsp; 
__________________________________________________________

