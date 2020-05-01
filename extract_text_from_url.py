from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def extract_text_from_url(url_value):
    if(url_value == 'NA' or "facebook.com" in url_value):
        return 'Not a valid URL'

    # read url    
    html = urlopen(url_value).read()
    soup = BeautifulSoup(html,features="lxml")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines and clean text
    text = ' '.join(chunk for chunk in chunks if chunk)

    # convert and remove unicode errors
    text = text.encode('ascii', 'ignore').decode('ascii')

    if isinstance(text,str):
        return text
    return 'Cannot extract text'

# test run
#url_value = 'https://www.timesnownews.com/india/article/woman-collecting-economic-census-data-attacked-in-kota-let-off-after-offering-proof-of-being-muslim-1-nabbed/543927Â â€¦'
#print(extract_text_from_url(url_value))