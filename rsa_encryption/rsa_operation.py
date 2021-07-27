"""

    Methods to perform RSA Encryption and Decryption.

    References:
         1) https://en.wikipedia.org/wiki/RSA_(cryptosystem)
         2) https://en.wikipedia.org/wiki/Least_common_multiple

"""
import sympy
from rsa_constants import *


#-----------------------------------------------------------------------------------------------#
#  Encryption and Decryption                                                                    #
#-----------------------------------------------------------------------------------------------#

def encrypt(n, e, m):
    """
        Encrypt (optionally padded) plaintext integer m using public key components n and e ->
            encrypted ciphertext ct = m^e mod(n)

        Return c
    """
    return pow(m, e, n)


def decrypt(n, d, c):
    """
        Decrypt encrypted ciphertext c using public key component n and private key exponent d ->
            decrypted plaintext integer m = c^d mod(n)

        Return m
    """
    return pow(c, d, n)


#-----------------------------------------------------------------------------------------------#
#  Key Generation                                                                               #
#-----------------------------------------------------------------------------------------------#

def generate_keys():
    """
        Generate private and public keys using the methods below.

        Return n and e (public key) and d (private key)
    """
    n, e, t = public_and_totient()
    d       = private_exponent(e, t)

    return n, e, d  


def public_and_totient():
    """
        Generate public key components n and e as well as carmichael totient t.
    """
    p, q = generate_primes()
    n    = public_modulus(p, q)
    t    = carmichael_totient(p, q)
    e    = public_exponent()

    if validated_public(e, t):
        return n, e, t
    else:
        return public_and_totient()


def generate_primes():
    """
        Generate unique prime integers p and q of different amounts of digits
        to make prime factoring more difficult.

        Return p and q
    """
    p = sympy.randprime(PRIME_LOWER, PRIME_UPPER)
    q = sympy.randprime(PRIME_LOWER, PRIME_UPPER)

    if validated_primes(p, q):
        return p, q
    else:
        return generate_primes()


def public_modulus(p, q):
    """
        Calculate public key modulus n as n = pq.

        Return n
    """
    return p * q


def carmichael_totient(p, q):
    """
        Calculate Carmichael Totient t = t(n). Since p and q are prime,
        t(n) in this context evaluates to lcm(p - 1, q - 1).

        Return t
    """
    return int(sympy.lcm(p - 1, q - 1))


def public_exponent():
    """
        Public key exponent e such that 1 < e < t and gcd(e, t) = 1.
        [Commonly 65,537, or 2^16 + 1]

        Return e
    """
    return ACTIVE_E


def private_exponent(e, t):
    """
        Calculate private key exponent d as the modular multiplicative inverse of e mod c(n).

        Return d
    """
    return int(sympy.mod_inverse(e, t))


#-----------------------------------------------------------------------------------------------#
#  Validation methods                                                                           #
#-----------------------------------------------------------------------------------------------#


def validated_primes(p, q):
    """
        Ensure generated primes satisfy the proper conditions.
    """
    r1 = unique_primes(p, q)
    r2 = different_digits(p, q)

    return r1 and r2


def unique_primes(p, q):
    """
        Validate that ->
            1) p and q are not the same

        Return result
    """
    return p != q


def different_digits(p, q):
    """
        Validate that ->
            1) p and q have a different number of digits.
    """
    p = str(p)
    q = str(q)
    d = abs(len(p) - len(q))

    return d != 0


def validated_public(e, t):
    """
        Validate that ->
            1) 1 < e < t
            2) gcd(e, t) = 1

        Return result
    """
    v1 = 1 < e < t
    v2 = sympy.gcd(e, t) == 1

    return v1 and v2
