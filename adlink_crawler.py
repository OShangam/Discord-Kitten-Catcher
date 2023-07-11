import requests
from bs4 import BeautifulSoup
import re
from mega_checker import valid_mega_url

discord_links = []
def ad_link(host):
    file = open("link/Mega_Links.txt", "w")

    with open('link/Discord_Links.txt', 'r') as link:
        for ligne in link:
            lien = ligne.strip()
            discord_links.append(lien)

    for i in range(len(discord_links)):
        url = discord_links[i]
        if "https://" in url:
            reqs = requests.get(url)
            html_content = reqs.text

            paste_link = re.search(f"link:\s+'(https?://{host}.*?)'", html_content)
            if paste_link:
                url = paste_link.group(1)
            else:
                print(f"The request has been denied.")
                pass

        reqs = requests.get(url)
        html = BeautifulSoup(reqs.text, 'html.parser')

        compteur = 0
        for link in html.find_all('a'):
            if "https://mega.nz/" in link.attrs['href']:
                if valid_mega_url(link.get('href')):
                    file.flush()
                    compteur += 1

                    file.write(link.get('href') + "\n")
                    print(f"Processing this link : {discord_links[i]} --> {url} {i}/{len(discord_links)} [{compteur} Mega found]")
                else:
                    print(f"{link.attrs['href']} is already banned.")