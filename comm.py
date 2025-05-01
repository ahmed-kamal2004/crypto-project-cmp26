

from server import Server
from sam import SeedAuthenticationModule
from sem import SeedEncryptionModule
from config import Config

class CommunicationModule:

    @staticmethod
    def initiate_communication(sender:Server, receiver:Server):

        y_sender = sender.generate_key()
        y_receiver = receiver.generate_key()

        sender.capture_key(y_receiver)
        receiver.capture_key(y_sender)

        return 


    @staticmethod
    def send_seeds(sender:Server,receiver:Server):

        message = sender.generate_seed()

        receiver.capture_seed(message)

        if sender.seed_is_captured() and receiver.seed_is_captured():
            return
        raise Exception("Error in sending seeds")
    

    @staticmethod
    def send_message(msg,sender:Server,receiver:Server):
        
        ## Initialize the LCG in every Server
        sender.create_lcg()
        receiver.create_lcg()


        block_size = Config.size
        indata_bytes = bytearray(msg.encode())
        for i in range(0, len(indata_bytes), block_size):
            block = indata_bytes[i:i+block_size]
            enc_msg = sender.encrypt(block)
            receiver.decrypt(enc_msg)

        receiver.write_msg_to_file()


        print(msg,"\n",receiver.get_message().decode())
        


