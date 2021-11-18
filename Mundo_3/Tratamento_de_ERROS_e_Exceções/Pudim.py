from urllib.request import Request, urlopen
from urllib.error import URLError

try:
    response = urlopen(Request("http://www.pudim.com.br/"))
except URLError:
    print('We failed to reach a server.')
else:
    print ('Website is working fine')
