import secrets
from sem import SeedEncryptionModule
from sam import SeedAuthenticationModule
from config import Config
from lcg import LinearCongruentialGenerator

class Server:


    def __init__(self):

        self.q = Config.q
        self.alpha = Config.alpha
        self.seed_bytes = Config.seed_bytes

        self.key = None
        self.x = None
        self.seed = None
        self.message = None

        self.lcg = None


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

    def encrypt(self,msg_stream):
        k = self.lcg.next()
        cipher_stream = (k ^ int.from_bytes(msg_stream, 'big'))
        cipher_byte_stream = cipher_stream.to_bytes((cipher_stream.bit_length() + 7) // 8,'big')
        return cipher_byte_stream

    def decrypt(self,enc_msg):
        k = self.lcg.next()
        cipher_stream = (k ^ int.from_bytes(enc_msg, 'big'))
        cipher_byte_stream = cipher_stream.to_bytes((cipher_stream.bit_length() + 7) // 8,'big')
        if not self.message:
            self.message = cipher_byte_stream
        else:
            self.message += cipher_byte_stream

    def create_lcg(self):
        if self.seed_is_captured():
            self.lcg = LinearCongruentialGenerator(self.seed)
        else:
            raise Exception("Capture Seed First")
        
    def get_message(self):
        return self.message

    def finish_sending(self):
        self.message = None

    def write_msg_to_file(self):
        with open(Config.out_file, 'w') as out_file:
            out_file.write(self.message.decode())
            out_file.close()