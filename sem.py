
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# Seed Encryption Module
class SeedEncryptionModule:

    IV = None

    @staticmethod
    def msg_encrypt(message,key):
        key_bytes = key.to_bytes(256 // 8, 'big')
        aesgcm = AESGCM(key_bytes)
        enc_message = aesgcm.encrypt(SeedEncryptionModule.get_iv(), message, associated_data=None)
        return enc_message
    

    @staticmethod
    def msg_decrypt(enc_message,key):
        key_bytes = key.to_bytes(256 // 8, 'big')
        aesgcm = AESGCM(key_bytes)
        message = aesgcm.decrypt(SeedEncryptionModule.get_iv(), enc_message, associated_data=None)
        return message

    @staticmethod
    def get_iv():
        if SeedEncryptionModule.IV == None:
            SeedEncryptionModule.IV = os.urandom(12)
        return SeedEncryptionModule.IV
