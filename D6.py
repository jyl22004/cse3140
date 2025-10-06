from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

with open('DecryptedSharedKey', 'rb') as f:
    key = f.read()


current_directory = os.getcwd()
for entry in os.listdir(current_directory):
    if entry.endswith('.encrypted'):
        f = open(entry,'rb+')
        
        iv = f.read(16)
        ciphertext = f.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(ciphertext)
        unpadded_data = unpad(decrypted_data, AES.block_size)
        str_data = unpadded_data.decode()

        new_file = entry.replace('.encrypted','')

        with open(new_file, 'w') as n:
            n.write(str_data)

        os.remove(entry)
