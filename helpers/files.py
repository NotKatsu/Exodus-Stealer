import os.path 

client: str = os.path.expanduser("~")

class Files: 
    def __init__(self) -> None:
        pass
    
    def path_exists() -> bool:
        if os.path.exists(client + "\\AppData\\Roaming\\Exodus"):
            return True
        else:
            return False
        