import requests, re, time, random
from colorama import init, Fore
init(convert=True)

def start():

    urls = ["https://discordservers.me/servers/search?term=Nitro&page=", "https://discordservers.me/servers/search?term=Giveaway&page="]
    numb = 1
    session = requests.Session()
    print(f"[{Fore.CYAN}>{Fore.RESET}] Input Discord Token")
    token = input(" > ")
    
    while True:
        if numb < 100:
            for url in urls:
                response = session.get(url + str(numb))
                if response.status_code != 404:
                    regex = re.search("https(:)\/\/discord.gg\/[a-zA-Z0-9]+", response.text)

                    if regex:
                        code = str(regex.group()).split("/")[3]
                        
                        headers = {
                            "Authorization": token
                        }

                        inviteResp = session.post(f"https://discordapp.com/api/v6/invites/{code}", headers=headers).json()
                        try:
                            if inviteResp["guild"]["name"]:
                                print(f"[{Fore.CYAN}Success{Fore.RESET}] Joined the server: {inviteResp['guild']['name']}")
                        except:
                            pass
                    else:
                        pass
                elif response.status_code == 404:
                    break
        else:
            break
        numb+=1
    input("")

if __name__ == "__main__":
    start()
