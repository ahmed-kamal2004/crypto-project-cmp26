
from lcg import LCG
from xor import XOR





# Stream Cipher Module:
class StreamCipherModule:

    @staticmethod
    def cipher(text,key):

        if len(key_stream) == len(cipher_text):
            key_stream = LCG.generate_key_stream(key)
            cipher_text = XOR.xor(text,key_stream)
            return cipher_text
        return None
