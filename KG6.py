from Crypto.PublicKey import RSA

key = RSA.generate(2048)
public_key = key.publickey()
private_key = key



with open('e.key', 'wb') as e:
    data = public_key.export_key()
    e.write(data)

with open('d.key', 'wb') as d:
    data = private_key.export_key()
    d.write(data)