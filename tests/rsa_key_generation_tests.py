"""

    Tests for the key generation methods in rsa_operation.py.

"""
import unittest
from rsa_encryption.rsa_operation import *


class TestKeyGeneration(unittest.TestCase):

    def test_unique_primes(self):
        """
            Ensure unique primes validator ->
                1) Returns True when unique primes UP and UQ are used.
                2) Returns False when the same prime (non-unique) NU is used.
        """
        r1 = unique_primes(UP, UQ)
        r2 = unique_primes(NU, NU)

        # 1
        self.assertTrue(r1)

        # 2
        self.assertFalse(r2)

    def test_validated_digits(self):
        """
            Ensure digits difference validator ->
                1) Returns True when different
                2) Returns False when same
        """
        r1 = different_digits(DP, DQ)
        r2 = different_digits(SP, SQ)

        # 1
        self.assertTrue(r1)

        # 2
        self.assertFalse(r2)

    def test_validated_public(self):
        """
            Ensure public exponent validator ->
                1) Returns True when 1 < e < t and gcd(e, t) = 1
                2) Returns False when 1 < e < t but gcd(e, t) != 1
                3) Returns False when e > t but gcd(e, t) = 1
        """
        r1 = validated_public(DE, T1)
        r2 = validated_public(DE, T2)
        r3 = validated_public(DE, T3)

        # 1
        self.assertTrue(r1)

        # 2
        self.assertFalse(r2)

        # 3
        self.assertFalse(r3)

    def test_generate_primes(self):
        """
            Ensure generated p and q ->
                1) Are prime
                2) Are integers
                3) Are not the same
                4) Have a different amount of digits
        """
        p, q = generate_primes()

        # 1
        self.assertTrue(sympy.isprime(p))
        self.assertTrue(sympy.isprime(q))

        # 2
        self.assertTrue(type(p) == int)
        self.assertTrue(type(q) == int)

        # 3
        self.assertTrue(p != q)

        # 4
        self.assertTrue(different_digits(p, q))

    def test_totient_type(self):
        """
            Ensure returned t ->
                1) Is an integer
        """
        p = TEST_P
        q = TEST_Q
        t = carmichael_totient(p, q)

        # 1
        self.assertTrue(type(t) == int)

    def test_private(self):
        """
            Ensure calculated d satisfies ->
                1) (d * e) mod(t) = 1 mod(t)
                2) d is an integer
        """
        p = TEST_P
        q = TEST_Q
        t = carmichael_totient(p, q)
        e = public_exponent()
        d = private_exponent(e, t)

        # 1
        self.assertTrue((d * e) % t == 1 % t)

        # 2
        self.assertTrue(type(d) == int)

    def test_private_random(self):
        """
            Ensure calculated d satisfies ->
                1) (d * e) mod(t) = 1 mod(t)
                2) d is an integer
        """
        p, q = generate_primes()
        t    = carmichael_totient(p, q)
        e    = public_exponent()
        d    = private_exponent(e, t)

        # 1
        self.assertTrue((d * e) % t == 1 % t)

        # 2
        self.assertTrue(type(d) == int)


if __name__ == '__main__':
    unittest.main()
