"""

    Methods to perform RSA Encryption and Decryption.

    References:
         1) https://en.wikipedia.org/wiki/RSA_(cryptosystem)
         2) https://en.wikipedia.org/wiki/Least_common_multiple

"""
import sympy
from rsa_encryption.rsa_constants import *


#-----------------------------------------------------------------------------------------------#
#  Message Encoding                                                                             #
#-----------------------------------------------------------------------------------------------#

def encode_message(message):
    """
        Encode string message as integer containing ASCII codes for each character separated by 
        an integer-encoded buffer. This is used since the RSA Algorithm requires m be an integer.

        Return encoded_message 
    """
    message_codes   = [str(ord(ch)) for ch in message]
    encoded_message = int(CODE_BUFFER.join(message_codes))

    return encoded_message


def decode_message(encoded_message):
    """
        Decode encoded integer message back to string message.

        Return decoded_message
    """
    message_codes   = str(encoded_message).split(CODE_BUFFER)
    message_chars   = [chr(int(code)) for code in message_codes]
    decoded_message = ''.join(message_chars)

    return decoded_message


#-----------------------------------------------------------------------------------------------#
#  Encryption and Decryption                                                                    #
#-----------------------------------------------------------------------------------------------#

def encrypt(n, e, m):
    """
        Encrypt (optionally padded) plaintext integer m using public key components n and e ->
        encrypted ciphertext ct = m^e mod(n)

        Return c
    """
    m = encode_message(str(m))
    c = pow(m, e, n)

    return c


def decrypt(n, d, c):
    """
        Decrypt encrypted ciphertext c using public key component n and private key exponent d ->
        decrypted plaintext integer m = c^d mod(n)

        Return m
    """
    m = pow(c, d, n)
    m = decode_message(m)

    return m


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

    for attempt in range(MAX_ITERATIONS):
        e = public_exponent()
        t = carmichael_totient(p, q)

        if validated_public(e, t):
            return n, e, t

    # This should never be reached in production.
    raise Exception('ERROR: Maximum iterations exceeded while generating public key and totient.')


def generate_primes():
    """
        Generate unique prime integers p and q of different amounts of digits
        to make prime factoring more difficult.

        Return p and q
    """
    for attempt in range(MAX_ITERATIONS):
        p = sympy.randprime(PRIME_LOWER, PRIME_UPPER)
        q = sympy.randprime(PRIME_LOWER, PRIME_UPPER)

        if validated_primes(p, q):
            return p, q

    # This should never be reached in production.
    raise Exception('ERROR: Maximum iterations exceeded while generating primes.')


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

        Return result
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

        Return result
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