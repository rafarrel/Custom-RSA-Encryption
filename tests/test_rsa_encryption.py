"""

    Tests for the encryption and decryption methods in rsa_operation.py.

"""
import unittest
from rsa_encryption.rsa_operation import *


class TestEncryption(unittest.TestCase):

    def test_encryption(self):
        """
            Ensure encrypted ciphertext c ->
                1) Is an integer
                2) Is not the same as original message
        """
        m = M_LARGE

        n, e, d = generate_keys()
        c       = encrypt(n, e, m)

        # 1
        self.assertTrue(type(c) == int)

        # 2
        self.assertTrue(c != m)

    def test_decryption(self):
        """
            Ensure decrypted message dm ->
                1) Is an integer
                2) Is the same as original message
        """
        m = M_LARGE

        n, e, d = generate_keys()
        c       = encrypt(n, e, m)
        dm      = decrypt(n, d, c)

        # 1
        self.assertTrue(type(dm) == str)

        # 2
        self.assertTrue(dm == str(m))

    def test_prime_lower_m_large(self):
        """
            Ensure two lowest unique primes after/including PRIME_LOWER ->
                1) Still successfully decrypt ciphertext
        """
        m  = M_LARGE

        p  = sympy.nextprime(PRIME_LOWER)
        q  = sympy.nextprime(p)

        n  = public_modulus(p, q)
        t  = carmichael_totient(p, q)
        e  = public_exponent()
        d  = private_exponent(e, t)
        c  = encrypt(n, e, m)
        dm = decrypt(n, d, c)

        # 1
        self.assertTrue(dm == str(m))


if __name__ == '__main__':
    unittest.main()