
<img src="https://i.ibb.co/5FBDP1s/title-keyhex.jpg" alt="title-keyhex" border="0">

> # KEYHEX

#### AES Encryption Python Script

The KeyHEX project is an interactive tool developed in Python that allows users to encrypt and decrypt messages using AES (Advanced Encryption Standard). The script's mission is to transform your message into an AES algorithm with SHA-256 in CFB mode that can only be decrypted with the encrypted code and password. KeyHEX was an experiment to study AES encryption.

_GUI development in progress._

## What is Cryptography?

Cryptography is the science of providing security and protection of information. It is used everywhere in our digital world: when you open a Web site, send an email or connect to the WiFi network. 

## AES (_Advanced Encryption Standard_).

<details>
<summary>
    <h4>Advanced Encryption Standard</h4>
</summary><br>

AES is a variant of the Rijndael block cipher developed by two Belgian cryptographers, `Joan Daemen` and `Vincent Rijmen`, who submitted a proposal to NIST during the AES selection process. Rijndael is a family of ciphers with different key and block sizes. For AES, NIST selected three members of the Rijndael family, each with a block size of 128 bits, but three different key lengths: 128, 192 and 256 bits.

AES is a symmetric encryption algorithm, which means that it uses the same key to encrypt and decrypt data. It operates on blocks of data and is designed to be fast and efficient on a wide variety of devices. AES replaced the old DES (Data Encryption Standard) encryption algorithm. 

_AES consists of several steps, including byte substitutions, row permutations, column permutations and key addition, all applied repeatedly in multiple rounds. These complex operations provide a robust security layer against a variety of known cryptographic attacks._
</details>

<details>
<summary>
    <h4>Description of the Ciphers</h4>
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

## Calculate SHA-256 Hash

|Input|Output     |
|-----|-----------|
|hello|2cf24dba5fb0a30e26e83b2ac5b5e29e1b161e5c1fa7425e79043062938b9824|

_The longer the encrypted message, the longer the hexadecimal code._

## Interface console:

<img src="https://i.ibb.co/GtmN7B2/interface-image1.png" alt="interface-image1" border="0">

## Video demo KeyHEX

[![Alt text](https://img.youtube.com/vi/2bGmIa1zv4A/0.jpg)](https://www.youtube.com/watch?v=2bGmIa1zv4A)

## License
 * [MIT](LICENSE)

## Technologies used:

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)&nbsp; 
__________________________________________________________

