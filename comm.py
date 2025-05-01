

from server import Server
from sam import SeedAuthenticationModule
from sem import SeedEncryptionModule

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
