import requests
from bs4 import BeautifulSoup
import re

discord_links = []
def ad_link(host):
    file = open("link1/Mega_Links.txt", "w")
    compteur = 0

    with open('link1/Discord_Links.txt', 'r') as link:
        for ligne in link:
            lien = ligne.strip()
            discord_links.append(lien)

    for i in range(len(discord_links)):
        url = discord_links[i]
        if "https://" in url:
            html_content = get_html_content(url)

            adlink = re.search(f"link:\s+'(https?://{host}.*?)'", html_content)
            mega = re.search(f"link:\s+'(https?://mega.*?)'", html_content)

            if adlink:
                url = adlink.group(1)

            elif mega:
                url = mega.group(1)

                file.flush()
                compteur += 1

                file.write(url + "\n")
                print(f"Processing this link : {discord_links[i]} --> {url} {i}/{len(discord_links)} [{compteur} Mega found]")
            else:
                print(f"The request has been denied.")
                pass


        reqs = requests.get(url)
        html = BeautifulSoup(reqs.text, 'html.parser')

        for link in html.find_all('a'):
            if "https://mega.nz/" in link.attrs['href']:
                file.flush()
                compteur += 1

                file.write(link.get('href') + "\n")
                print(f"Processing this link : {discord_links[i]} --> {url} {i}/{len(discord_links)} [{compteur} Mega found]")

def get_html_content(url):
    reqs = requests.get(url)
    html_content = reqs.text

    return html_content