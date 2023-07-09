import requests
import re

mega_links = []
file = open("Mega Lien.txt", "r")
file_valid = open("Mega_Valid.txt", "w")

with open('Mega Lien.txt', 'r') as link:
    for ligne in link:
        lien = ligne.strip()
        mega_links.append(lien)

def valid_mega_url():
    for i in range(len(mega_links)):
        url = mega_links[i]

        if "https://mega.nz/" in url:
            reqs = requests.get(url)
            html_content = reqs.text
            mega_checker = re.search(r'<meta\s+property="og:description"\s+content="[^"]*(\d+)', html_content)

            if mega_checker:
                # Pas Ban
                print(f"Mega={mega_links[i]} VALID= TRUE")
                file_valid.write((mega_links[i]) + "\n")
            else:
                # Ban
                print(f"Mega={mega_links[i]} VALID= FALSE")

valid_mega_url()