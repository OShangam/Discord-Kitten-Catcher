import requests
from bs4 import BeautifulSoup
import re
from mega_checker import valid_mega_url

discord_links = []

file = open("Mega Lien.txt", "w")

with open('Lien.txt', 'r') as link:
    for ligne in link:
        lien = ligne.strip()
        discord_links.append(lien)

for i in range(len(discord_links)):
    url = discord_links[i]
    if "https://" in url:
        reqs = requests.get(url)
        html_content = reqs.text

        paste_link = re.search(r"link:\s+'(https?://pastelink.*?)'", html_content)
        if paste_link:
            url = paste_link.group(1)
        else:
            print("Pastelink not found.")

    reqs = requests.get(url)
    html = BeautifulSoup(reqs.text, 'html.parser')
    urls = []

    compteur = 0
    for link in html.find_all('a'):
        if "https://mega.nz/" in link.attrs['href']:
            file.flush()
            compteur += 1

            file.write(link.get('href') + "\n")
            print(f"Processing this link : {discord_links[i]} --> {url} {i}/{len(discord_links)} [{compteur} Mega found] VALID = {valid_mega_url()}")


