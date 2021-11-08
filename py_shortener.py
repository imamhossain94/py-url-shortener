import os
import pyshorteners
from dotenv import load_dotenv
load_dotenv()


def adf_ly():   # 50% Working
    import pyshorteners
    s = pyshorteners.Shortener(api_key=os.environ.get('ADF_API_KEY', ''),
                               user_id=os.environ.get('ADF_USER_ID', ''),
                               domain='test.us', group_id=None, type='2')
    x = s.adfly.short('http://www.facebook.com')
    print(x)


def bit_ly():   # Not Working
    s = pyshorteners.Shortener(api_key=os.environ.get('BIT_API_KEY', ''))
    x = s.bitly.short('http://www.google.com')
    print(x)
    # y = s.bitly.expand('https://bit.ly/TEST')
    # print(y)


def cutt_ly():  # Working
    s = pyshorteners.Shortener(api_key=os.environ.get('CUTTLY_API_KEY', ''))
    x = s.cuttly.short('http://www.google.com')
    y = s.cuttly.expand('https://cutt.ly/ATrGn3J')
    print(x)
    print(y)


def chilp_it():   # 50% Working
    s = pyshorteners.Shortener()
    x = s.chilpit.short('http://www.google.com')
    print(x)
    # y = s.chilpit.expand('http://chilp.it/ed646a3')
    # print(y)


def clck_ru():  # Working
    s = pyshorteners.Shortener()
    x = s.clckru.short('http://www.google.com')
    y = s.clckru.expand('https://clck.ru/0v')
    print(x)
    print(y)


def da_gd():  # 50% Working
    s = pyshorteners.Shortener()
    x = s.dagd.short('http://www.google.com')
    print(x)
    # y = s.dagd.expand('https://da.gd/2UoqA')
    # print(y)


def git_io():   # Working
    s = pyshorteners.Shortener()
    x = s.gitio.short('https://github.com/')
    y = s.gitio.expand('https://git.io/p6oxyA')
    print(x)
    print(y)


def ls_gd():    # Working
    s = pyshorteners.Shortener()
    x = s.isgd.short('http://www.google.com')
    y = s.isgd.expand('https://is.gd/WzFWtC')
    print(x)
    print(y)


def os_db():    # 50% Working
    s = pyshorteners.Shortener()
    x = s.osdb.short('http://www.google.com')
    print(x)
    # y = s.osdb.expand('http://osdb.link/6ay6')
    # print(y)


def qps_ru(): # 50% Working
    s = pyshorteners.Shortener()
    x = s.qpsru.short('http://google.com')
    print(x)
    # y = s.qpsru.expand('https://qps.ru/HTbs9')
    # print(y)


def short_io():  # Not Working
    s = pyshorteners.Shortener(api_key=os.environ.get('SHORT_API_KEY', ''))
    x = s.shortcm.short('http://google.com')
    print(x)
    # y = s.shortcm.expand('https://qps.ru/HTbs9')
    # print(y)


def tiny_cc():  # Working
    s = pyshorteners.Shortener()
    x = s.tinyurl.short('http://www.google.com')
    print(x)
    y = s.tinyurl.expand('https://tinyurl.com/8wa5w2o')
    print(y)

tiny_cc()
