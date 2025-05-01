import secrets
from sem import SeedEncryptionModule
from sam import SeedAuthenticationModule
from config import Config

class Server:


    def __init__(self):

        self.q = Config.q
        self.alpha = Config.alpha
        self.seed_bytes = Config.seed_bytes

        self.key = None
        self.x = None
        self.seed = None


        pass


    def generate_key(self):
        self.x = secrets.randbelow(self.q - 3) + 2
        return pow(self.alpha,self.x,self.q)
    
    def capture_key(self,y):
        self.key = pow(y,self.x,self.q)


    def generate_seed(self):
        self.seed = secrets.token_bytes(self.seed_bytes)
        digest = SeedAuthenticationModule.create_digest(self.seed,self.key)
        message = self.seed + digest
        enc_message = SeedEncryptionModule.msg_encrypt(message,self.key)
        return enc_message

    def capture_seed(self,enc_message):
        message = SeedEncryptionModule.msg_decrypt(enc_message,self.key)
        seed, state = SeedAuthenticationModule.check_digest(message,self.key)
        if not state:
            raise Exception("Not Authenticated")
        self.seed = seed


    def key_is_captured(self):
        return self.key != None
    
    def seed_is_captured(self):
        return self.seed != None

    def encrypt():
        pass

    def decrypt():
        pass


