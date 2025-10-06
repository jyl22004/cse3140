import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

encrypted_f = sys.argv[1]
with open(encrypted_f, 'rb') as f:
    encrypted_key = f.read()

with open('d.key','rb') as d:
    data = d.read()
    private_key = RSA.import_key(data)

key_cipher = PKCS1_OAEP.new(private_key)
original_key = key_cipher.decrypt(encrypted_key)

with open('DecryptedSharedKey','wb') as dsk:
    dsk.write(original_key)

