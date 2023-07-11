import requests
import re

def valid_mega_url(mega_links):
    for i in range(len(mega_links)):
        url = mega_links

        if "https://mega.nz/" in url:
            reqs = requests.get(url)
            html_content = reqs.text
            mega_checker = re.search(r'<meta\s+property="og:description"\s+content="[^"]*(\d+)', html_content)

            if mega_checker:
                # Pas Ban
                return True
            else:
                # Ban
                return False


