"""

    Tests for the encode and decode methods in rsa_operation.py.

"""
import unittest
from rsa_encryption.rsa_constants import *
from rsa_encryption.rsa_operation import *

class TestEncoding(unittest.TestCase):

    def test_encode_and_decode_message_basic(self):
        """
            Ensure encoded message m ->
                1) Is an integer
                2) Is not the same as original message
                3) Can be successfully decoded
        """
        m = M_BASIC

        encoded_m = encode_message(m)
        decoded_m = decode_message(encoded_m)

        # 1
        self.assertTrue(type(encoded_m) == int)

        # 2
        self.assertTrue(encoded_m != m)

        # 3
        self.assertTrue(decoded_m == m) 

    def test_encode_decode_message_buffer(self):
        """
            Ensure encoded message m ->
                1) Can be successfully decoded if it contains characters/
                   character combos with codes close to the buffer (i.e.
                   90 (Z), 9090 (ZZ), 100 (@), etc.)
        """
        m = M_BUFFER

        encoded_m = encode_message(m)
        decoded_m = decode_message(encoded_m)

        # 1
        self.assertTrue(decoded_m == m) 


if __name__ == '__main__':
    unittest.main()