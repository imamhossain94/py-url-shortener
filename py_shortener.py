import os
import pyshorteners
from dotenv import load_dotenv
load_dotenv()


def cutt_ly():
    s = pyshorteners.Shortener(api_key=os.environ.get('CUTTLY_API_KEY', ''))
    x = s.cuttly.short('http://www.google.com')
    y = s.cuttly.expand('https://cutt.ly/ATrGn3J')
    print(x)
    print(y)


cutt_ly()

