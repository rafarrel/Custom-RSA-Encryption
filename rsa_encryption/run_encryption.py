"""

    Basic commandline interface to run the encryption implementation. 
    Simply navigate to this directory and run: python run_encryption.py

"""
from rsa_operation import *


m = input('Enter message to encrypt: ')
print()

n, e, d = generate_keys()
c       = encrypt(n, e, m)
dm      = decrypt(n, d, c)

print('Original message: {}'.format(m))
print('Ciphertext: {}'.format(c))
print('Decrypted message: {}'.format(dm))