import requests
from bs4 import BeautifulSoup
import re

discord_links = []
def ad_link(host, last_mega):
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
                compteur += 1

                write_system(file, url)
                print(f"Processing this link : {discord_links[i]} --> {url} {i}/{len(discord_links)} [{compteur} Mega found]")
            else:
                print(f"The request has been denied.")
                pass

        ad_link_2 = get_adlink(url, host)
        mega_link = get_megalink(url, "mega.nz")

        if mega_link == last_mega:
            print(f"Already Banned.")
            return

        if mega_link:
            compteur += 1

            write_system(file, mega_link)
            print(f"Processing this link : {discord_links[i]} --> {url} {i}/{len(discord_links)} [{compteur} Mega found]")

        elif ad_link_2 is not None: #NoneType error :)))))
            mega_link = get_megalink(ad_link_2, "mega.nz")

            if mega_link:
                compteur += 1

                write_system(file, mega_link)
                print(f"Processing this link : {discord_links[i]} --> {ad_link_2} {i}/{len(discord_links)} [{compteur} Mega found]")
            else:
                print("I am sorry but there is no mega link here...")


def write_system(file, url):
    file.flush()
    file.write(url + "\n")


def get_megalink(url, host):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        link_pattern = re.compile(f'https://{host}(.*)')
        links = soup.find_all('a', href=link_pattern)

        for link in links:
            return link['href']

def get_adlink(url, host):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        link_pattern = re.compile(f'https://{host}(.*)')
        links = soup.find_all('a', href=link_pattern)

        if links:
            return links[0]['href']
def get_html_content(url):
    reqs = requests.get(url)
    html_content = reqs.text

    return html_content