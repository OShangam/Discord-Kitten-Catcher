import requests
import json
import re

liste = []
url = []
def discord(channel, discord_token, host):
    # file = open('link1/Discord_Links.txt', 'w', encoding='utf-8')
    file = open('link1/Discord_Links.txt', 'w')

    headers = {
        "authorization":discord_token
    }

    id_message = None

    while True:

        if id_message:
            r = requests.get(f"https://discord.com/api/v9/channels/{channel}/messages?before={id_message}&limit=100", headers=headers)
        else:
            r = requests.get(f"https://discord.com/api/v9/channels/{channel}/messages?limit=100", headers=headers)
        try:
            requests_content = json.loads(r.text)
            id_message = requests_content[-1]["id"]

        except Exception as e:
            print(f"[#0001] Error: {e}, the program can continue")
            break

        for i in range(len(requests_content)):
            content = requests_content[i]["content"].replace('\u200b', '')  # Remove zero-width space
            liste.append(content)

    for i in range(len(liste)):
        try:
            url_filtered = re.findall(fr"(?P<url>https?://{host}\S+)", liste[i])
            for i in url_filtered:
                url.append(i)
        except Exception as e:
            print(f"[#0002] Error: {e}, the program can continue")
            pass

    for i in url:
        file.flush()
        file.write(i + "\n")
