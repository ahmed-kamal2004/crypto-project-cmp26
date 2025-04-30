


import hmac
from config import Config
import hashlib


class SeedAuthenticationModule:
    @staticmethod
    def create_digest(message,key):
        key_bytes = key.to_bytes((key.bit_length() + 7) // 8 or 1, 'big')
        h = hmac.new(key_bytes ,message,hashlib.sha256)
        digest = h.hexdigest()
        digest_bytes = bytes.fromhex(digest)
        return digest_bytes



    @staticmethod
    def check_digest(message_with_digest,key):
        digest_received = message_with_digest[Config.seed_bytes:]
        message = message_with_digest[:Config.seed_bytes] 
        key_bytes = key.to_bytes((key.bit_length() + 7) // 8 or 1, 'big')
        h = hmac.new(key_bytes ,message,hashlib.sha256)
        digest_calculated_hex = h.hexdigest()
        digest_calculated = bytes.fromhex(digest_calculated_hex)
        if digest_received == digest_calculated:
            return message , True
        return message, False


