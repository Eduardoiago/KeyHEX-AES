
<img src="https://i.ibb.co/5FBDP1s/title-keyhex.jpg" alt="title-keyhex" border="0">

# KEYHEX

#### Script python de criptografia EAS

O projeto KeyHEX é uma ferramenta interativa desenvolvida em `Python` que permite aos usuários criptografar e descriptografar mensagens usando AES (Advanced Encryption Standard). O script tem como missão transformar sua mensagem em algoritmo AES em modo CFB que só poderá ser descriptografado com o código criptografado e a senha. O KeyHEX foi um experimento de estudo sobre criptografia AES, menu e aplicações GUI. 

## AES (_Advanced Encryption Standard_).

<details>
<summary>Criptografia AES</summary>

O AES é um algoritmo de criptografia simétrica, o que significa que ele usa a mesma chave para criptografar e descriptografar os dados. Ele opera em blocos de dados e foi projetado para ser rápido e eficiente em uma ampla variedade de dispositivos.

O AES substituiu o antigo algoritmo de criptografia DES (Data Encryption Standard).
O AES opera em diferentes tamanhos de chave, sendo os mais comuns 128, 192 e 256 bits. Quanto maior a chave, mais difícil é para um atacante realizar um ataque de força bruta bem-sucedido. Na prática, o AES com uma chave de 128 bits é considerado seguro para a maioria das aplicações, mas chaves maiores podem ser preferíveis para cenários de alta segurança.

_O AES consiste em várias etapas, incluindo substituições de bytes, permutações de linhas, permutações de colunas e adição de chaves, todas aplicadas repetidamente em múltiplas rodadas. Essas operações complexas fornecem uma camada de segurança robusta contra uma variedade de ataques criptográficos conhecidos._
</details>
__________________________________________________________

- ## Requerimentos:

#### Instalando bibliotecas

``` shell
    pip install cryptography os
    pip install os
    pip install tqdm
```
A biblioteca Python `cryptography` é uma ferramenta poderosa para a implementação de criptografia e segurança em aplicativos Python. Ela oferece suporte a uma ampla gama de algoritmos criptográficos, como AES, RSA, HMAC e muito mais.

The `os` library in Python provides an interface for interacting with the underlying operating system. 

Também foi usado a biblioteca `tqdm` para gerar uma barra de progresso.

## Functionalities:

1. Criptografar mensagens, senhas e dados pessoais: o usuário pode inserir uma mensagem e uma senha para criptografá-la.

2. Descriptografar mensagem: o usuário pode inserir uma mensagem criptografada (em hexadecimal) e uma senha para descriptografá-la.

3. Ele utiliza o algoritmo AES em modo CFB (_Cipher Feedback Mode_) para criptografar os dados. Além disso, utiliza _PBKDF2_ para derivar a chave de uma senha fornecida.

## Technologies used:

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)&nbsp; 

## Interface console:

## Interface GUI:

## Video demo KeyHEX

[![Alt text](https://img.youtube.com/vi/2bGmIa1zv4A/0.jpg)](https://www.youtube.com/watch?v=2bGmIa1zv4A)

## License
 * [MIT](LICENSE)
__________________________________________________________
