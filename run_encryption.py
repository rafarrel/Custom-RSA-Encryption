"""

    Basic commandline interface to run the encryption implementation. 
    Simply navigate to this directory and run: python run_encryption.py "MESSAGE"

"""
import sys
import textwrap
from rsa_encryption.rsa_operation import *


try:
    # Argument Parsing
    if len(sys.argv) < 2:
        raise ValueError('ERROR: No message provided')
    elif len(sys.argv) > 2:
        raise ValueError('ERROR: Too many arguments')
    else:
        m = sys.argv[1]

    # Encryption/Decryption
    n, e, d = generate_keys()
    c       = encrypt(n, e, m)
    dm      = decrypt(n, d, c)

    # Display Results
    print('-'*70)
    print('Original message: {}'.format(m))
    print('-'*70)
    wrapper = textwrap.TextWrapper(width=70)
    print(wrapper.fill(text='Ciphertext: ' + str(c)))
    print('-'*70)
    print('Decrypted message: {}'.format(dm))
    print('-'*70)
except ValueError as verr:
    print(verr)
except:
    print('Uh-oh, something went wrong. Submit a pull request \
           and I can fix it right away!')