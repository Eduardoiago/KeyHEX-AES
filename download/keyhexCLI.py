P=range
G='\nPress ENTER to return to the Menu.'
D=len
B=input
A=print
from cryptography.hazmat.backends import default_backend as E
from cryptography.hazmat.primitives import padding as H
from cryptography.hazmat.primitives.ciphers import Cipher as I,algorithms as F,modes as J
from cryptography.hazmat.primitives import hashes as K
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as L
import os
from tqdm import tqdm as M
def Q(message,password):
	C=os.urandom(16);T=L(algorithm=K.SHA256(),length=32,salt=C,iterations=100000,backend=E());U=T.derive(password.encode());G=H.PKCS7(F.AES.block_size).padder();A=G.update(message.encode())+G.finalize();N=os.urandom(16);V=I(F.AES(U),J.CFB(N),backend=E());O=V.encryptor()
	with M(total=D(A),desc='Encrypting')as W:
		B=b'';Q=1024
		for R in P(0,D(A),Q):S=A[R:R+Q];X=O.update(S);B+=X;W.update(D(S))
		B+=O.finalize()
	return C+N+B
def R(encrypted_data,password):
	A=encrypted_data;S=A[:16];T=A[16:32];B=A[32:];U=L(algorithm=K.SHA256(),length=32,salt=S,iterations=100000,backend=E());V=U.derive(password.encode());W=I(F.AES(V),J.CFB(T),backend=E());G=W.decryptor()
	with M(total=D(B),desc='Decrypting')as X:
		C=b'';N=1024
		for O in P(0,D(B),N):Q=B[O:O+N];Y=G.update(Q);C+=Y;X.update(D(Q))
		C+=G.finalize()
	R=H.PKCS7(F.AES.block_size).unpadder();Z=R.update(C)+R.finalize();return Z.decode()
def S():N();A(C);A('♦  KEYHEX™  ♦');A(C);A('Github: https://github.com/Eduardoiago');A('Developed by Eduardo Iago | Version 1.0.0\n');A('The tool mission is to transform your message into an AES algorithm with SHA-256 in CFB mode that can only be decrypted with the encrypted code and password.\n');A('Before encrypting your messages and links, the tool processes SubBytes, ShiftRows, MixColumns and AddRoundKey. Remember to use strong passwords.\n');A('Visit the project documentation (https://github.com/Eduardoiago/KeyHEX-AES) to better understand how keyHEX works.');B(G)
def N():os.system('clear'if os.name=='posix'else'cls')
T='          1. Encrypt in AES'
U='          2. Decrypt in AES'
V='          3. Exit\n'
W='          Choose an option: '
X='===== keyHEX ===========================[SHA]256==============='
Y='===== keyHEX ================ Decrypted message ==============='
C='==============================================================='
Z='\n          Type the message: '
a='\n          Enter the encrypted message (in hexadecimal): '
O='\n          Enter the password: '
def b():
	E=' '
	while True:
		N();A('       \n              \n                     ♦  KEYHEX™ version 1.0 ♦\n              \n                     ██ ▄█▀▓█████▓██   ██▓ ██░ ██ ▓█████ ▒██   ██▒\n                     ██▄█▒ ▓█   ▀ ▒██  ██▒▓██░ ██▒▓█   ▀ ▒▒ █ █ ▒░\n                    ▓███▄░ ▒███    ▒██ ██░▒██▀▀██░▒███   ░░  █   ░\n                    ▓██ █▄ ▒▓█  ▄  ░ ▐██▓░░▓█ ░██ ▒▓█  ▄  ░ █ █ ▒ \n                    ▒██▒ █▄░▒████▒ ░ ██▒▓░░▓█▒░██▓░▒████▒▒██▒ ▒██▒\n                    ▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒  ▒ ░░▒░▒░░ ▒░ ░▒▒ ░ ░▓ ░\n                    ░ ░▒ ▒░ ░ ░  ░▓██ ░▒░  ▒ ░▒░ ░ ░ ░  ░░░   ░▒ ░\n                    ░ ░░ ░    ░   ▒ ▒ ░░   ░  ░░ ░   ░    ░    ░  \n                    ░  ░      ░  ░░ ░      ░  ░  ░   ░  ░ ░    ░  \n                                  ░ ░                         \n                    ==============================================\n                           AES Cryptography | SHA-256 in CFB mode  \n                    ==============================================           \n        ');A(T);A(U);A(V);D=B(W)
		if D=='1':I=B(Z);F=B(O);A(E);H=Q(I,F);A(E);A(X);A(H.hex());A(C);B(G)
		elif D=='2':H=bytes.fromhex(B(a));F=B(O);A(E);J=R(H,F);A(E);A(Y);A(J);A(C);B(G)
		elif D=='3':A('\nBye!');break
		elif D=='--info':S()
		else:A(C);A('\nInvalid option! Choose a valid option.');A(C)
if __name__=='__main__':b()
