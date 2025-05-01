
from server import Server
from config import Config
from comm import CommunicationModule


if __name__ == "__main__":

    # Initialize

    indata = None

    with open("input.txt") as input_file:
        indata = input_file.read()
        input_file.close()

    
    ## (Mandatory)
    Config.load()

    sender = Server()
    receiver = Server()

    ## Apply Diffe-Helman Algorithm

    CommunicationModule.initiate_communication(sender,receiver)

    ## Exchange Seeds (Needs Encryption)

    CommunicationModule.send_seeds(sender,receiver)

    ## Start Message Sharing
    CommunicationModule.send_message(indata,sender,receiver)

    



    

    


    



