from urllib.parse import urlparse
import re

def is_url(url):
    try:
        validURL = False
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        result = urlparse(url)

        if result and re.match(regex, url) is not None:
            validURL = True
        else:
            validURL = False

        return validURL
    except:
        return False

def getURL():
    url = "https://reqres.in/api/users?page=2"
    isUrl = is_url(url)
    invalidURL = False

    #print("Valid URL: " + str(isUrl))

    if isUrl:
        invalidURL = False
    else:
        invalidURL = True
        print("Invalid url!")

    return invalidURL, url