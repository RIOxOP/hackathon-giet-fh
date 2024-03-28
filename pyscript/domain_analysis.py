import whois
from datetime import datetime
from bs4 import BeautifulSoup
import random
import requests
def domain_analysis(url):
    def getHtmlDocument(url, headers):
        response = requests.get(url, headers=headers)
        return response.text

    def generate_user_agent() -> str:
        a = random.randint(63, 89)
        b = random.randint(1, 3200)
        c = random.randint(1, 140)
        user_agent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{a}.0.{b}.{c} Safari/537.3'
        return user_agent

    headers = {
        'User-Agent': generate_user_agent()
    }
    html_document = getHtmlDocument(url, headers)

    w = whois.whois(url)



    # get URL length
    url_len = len(url)

    def https_check(url) -> int:
        if url.startswith("https"):
            return 1
        else:
            return -10

    soup = BeautifulSoup    (html_document, 'html.parser')
    #get domain age
    creation_date = w.get('creation_date', None)
    # Ensure creation_date is a datetime object, not a list
    domain_age = 0
    if creation_date:
        if isinstance(creation_date, list):
            creation_date = min(creation_date)
        domain_age = (datetime.now() - creation_date).days
        domain_age /= 365.25


    def use_iframe(soup):
        iframes = soup.find_all('iframe')
        return len(iframes)

    def popup_window_has_text_field(soup):
        """
        Returns 1 if a pop-up window with text field exists, 0 otherwise
        """
        popups = soup.find_all('div', {'class': 'popup'})
        for popup in popups:
            if popup.find('input', {'type': 'text'}):
                return 1
    
        return 0
    def abnormal_url(url, w) -> int:
        """
        Returns 1 if the hostname is not in the URL, 0 otherwise.
        """
        host_name = w.domain.split('.')[0]
        if host_name not in url:
            return 1
        else:
            return 0

    https_check(url)
    use_iframe(soup)
    popup_window_has_text_field(soup)
    abnormal_url(url, w)
    def initial_score(url):
        return (url_len / 2) + (https_check(url) * 20) - (popup_window_has_text_field(soup) * 10) + (use_iframe(soup) * 10) + (abnormal_url(url, w) * 10) + domain_age

    if(initial_score(url) < 10):
        print(40)
    else:
        print((initial_score(url)))