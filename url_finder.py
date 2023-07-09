import requests
import json
import re

liste = []
url = []
file = open('Lien.txt', 'w')
def trouve(channel):
    headers = {
        "authorization":"MTEyNzI3OTQyMjI2MTcwMjcyNg.Gg_iG9.IPg-nv5VzzzGzQqdzW6cVbeY-6BKOBfd2_e_VA"
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
        except:
            break

        for i in range(len(requests_content)):
            liste.append(requests_content[i]["content"])

    for i in range(len(liste)):
        try:
            url_filtered = re.findall("(?P<url>https?://\S+)", liste[i])
            for i in url_filtered:
                url.append(i)
        except:
            pass

    for i in url:
        file.write(i + "\n")


trouve(1071775785326760026)