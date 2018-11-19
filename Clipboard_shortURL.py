from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection
#expand URL

import requests
#check URL

import pyperclip
#clipboard

def expandURL( url ):
    """
    convert URL shortening in clipboard to original URL

    Parameters
    ----------
    url : string
        URL shortening

    Returns
    ----------
    return_url : string
        original URL
    """

    #urlparse is tuple which has 6 elements for URL
    #o.netloc is Hostname of URL   EX)www.test.com
    #o.path is the Path            EX)/home/sample.pdf
    o = urlparse(url)

    #If URL is HTTPS, getheader( 'location' ) add Port-number to object
    #For that reason, I separated HTTP and HTTPS
    if o.scheme == 'https':
        con = HTTPSConnection( o.netloc )
    else:
        con = HTTPConnection( o.netloc )

    con.request( 'HEAD', o.path )
    res = con.getresponse()

    #get URL
    return_url = res.getheader( 'location' )
    if return_url == None:
        return url
    return return_url


def checkURL( url ):
    """
    check if URL exists

    Parameters
    ----------
    url : string
        URL
    """
    res = requests.get( url )

    #If the URL is invalid, forcibly terminate
    res.raise_for_status()

    return



def main():

    #get URL form clipboard
    delete spaces if end of string is spaces
    short_url = pyperclip.paste().rstrip( )

    #check URL
    checkURL( short_url )

    #at 1st, get expand URL
    expand_url = expandURL( short_url )


    #until you get original URL
    while expand_url != short_url:
        short_url = expand_url
        expand_url = expandURL( short_url )


    #copy original URL to clipboard
    pyperclip.copy( expand_url )


if __name__ == '__main__':
    main()
