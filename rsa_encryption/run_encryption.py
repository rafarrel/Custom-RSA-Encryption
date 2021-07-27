from rsa_operation import *

m = int(input('Enter integer m to encrypt (up to approximately 2^500) safely: '))

n, e, d = generate_keys()
c       = encrypt(n, e, m)
dm      = decrypt(n, d, c)

print('Original message: {}'.format(m))
print('Ciphertext: {}'.format(c))
print('Decrypted message: {}'.format(dm))