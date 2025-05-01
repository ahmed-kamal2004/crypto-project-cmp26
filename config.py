
import json

FILE_NAME="config.json"

class Config:
    seed_bytes = None
    q = None
    alpha = None
    a = None
    c = None
    m = None
    size = None
    out_file = None

    def load():
        
        with open(FILE_NAME) as config_file:
            app_config = json.loads(config_file.read())
            config_file.close()
            Config.seed_bytes = app_config["seed_bytes"]
            Config.alpha = app_config["alpha"]
            Config.q = app_config["q"]
            Config.a = app_config["a"]
            Config.c = app_config["c"]
            Config.m = app_config["m"]
            Config.size = app_config["size"]
            Config.out_file = app_config["out_file"]
            
