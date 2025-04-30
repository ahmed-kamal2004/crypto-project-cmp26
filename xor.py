
class XOR:

    @staticmethod
    def xor(text, keystream):
        ciphertext = bytearray()
        for p, k in zip(text, keystream):
            ciphertext.append(p ^ k)

        return bytes(ciphertext)