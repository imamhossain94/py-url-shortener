import os
import requests
from dotenv import load_dotenv
load_dotenv()


# https://cutt.ly/
# Create Api Key
def cuttly(url):
    api_key = os.environ.get('CUTTLY_API', '')
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    data = requests.get(api_url).json()["url"]
    if data["status"] == 7:
        shortened_url = data["shortLink"]
        return shortened_url
    else:
        return "error"


shortenUrl = cuttly("https://towardsdatascience.com/best-apis-for-url-shortening-using-python-2db09d1f86f0")

print(shortenUrl)   # https://cutt.ly/8TrzX2Q https://cutt.ly/LTrxAtE
