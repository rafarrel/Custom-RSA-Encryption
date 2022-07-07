"""

    Constants for rsa_encryption.py and its tests.

"""

#------------------------------------------------------------------------------------------------------------#
# Operation                                                                                                  #
#------------------------------------------------------------------------------------------------------------#

# Encoding/Decoding
CODE_BUFFER = '9009'           # Used to separate ASCII codes in encoded message. Guaranteed to not match or
                               # disrupt any code in an encoded message (as codes go up to 255 and there is
                               # no code 900).

MAX_ITERATIONS = 1000          # Maximum iterations for re-generating components that don't pass validation. If
                               # exceeded, an error is raised and the application force quits. This should never
                               # happen in production and is only included as a safety check.

# Defaults
DEFAULT_E = 65537              # Commonly chosen for a balance of performance and security (DO NOT CHANGE).

# Prime Generation
PRIME_LOWER = 2 ** 1000        # Inclusive     -> Arbitrary lower bound for balance of performance and security.
PRIME_UPPER = 2 ** 1100        # Not inclusive -> Arbitrary upper bound for balance of performance and security.

# Public Key Generation
ACTIVE_E = DEFAULT_E           # Active e value to be used.

#------------------------------------------------------------------------------------------------------------#
# Testing                                                                                                    #
#------------------------------------------------------------------------------------------------------------#

# Unique Primes
UP = 10067                     # Arbitrary prime which is unique from UQ.
UQ = 11593                     # Arbitrary prime which is unique from UP.

NU = 11621                     # Arbitrary prime to test that non-unique primes return false.

# Validated Digits
DP = 52153                     # Arbitrary prime which has a different amount of digits than DQ.
DQ = 501233                    # Arbitrary prime which has a different amount of digits than DP.

SP = 50051                     # Arbitrary prime which has the same amount of digits as SQ.
SQ = 50359                     # Arbitrary prime which has the same amount of digits as SP.

# Validated Public
DE = DEFAULT_E                 # Default e for testing conditions.

T1 = 294487588                 # Arbitrary totient such that 1 < e < T1 and gcd(e, T1) = 1.
T2 = 5000001233700000024672    # Arbitrary totient such that 1 < e < T2 but gcd(e, T2) != 1.
T3 = 19996                     # Arbitrary totient such that T3 > e and gcd(e, T2) = 1.

# Generate Public Key
TEST_P = 32771                 # Anything above satisfies lcm specifications (see lower_bound_proof).
TEST_Q = 32779                 # Next prime number after TEST_P.

# Encoding/Decoding
M_BASIC  = "This is a test!"   # Basic arbitrary string message for testing encoding/decoding functionality.
M_BUFFER = "ZZ@9009@¾ÈŒZ@d9"   # Arbitraty string message containing characters with codes close to the buffer.

# Encryption/Decryption
M_LARGE = 2 ** 300             # Arbitrary large value for m (reasonable upper bound for guaranteed encryption).