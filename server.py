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
        enc_seed = SeedEncryptionModule.seed_encrypt(self.seed,self.key)
        digest = SeedAuthenticationModule.create_digest(self.seed,self.key)
        message = enc_seed + digest
        return message

    def capture_seed(self,message):
        enc_seed, state = SeedAuthenticationModule.check_digest(message,self.key)
        if not state:
            raise Exception("Not Authenticated")
        self.seed = SeedEncryptionModule.seed_decrypt(enc_seed,self.key)


    def key_is_captured(self):
        return self.key != None
    
    def seed_is_captured(self):
        return self.seed != None

    def encrypt():
        pass

    def decrypt():
        pass


