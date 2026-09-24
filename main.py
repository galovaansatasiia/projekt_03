import requests
from bs4 import BeautifulSoup


url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"


def get_election_results(url):
    response = requests.get(url)
    response.encoding = "utf-8"

    return response.text

def parse_election_results(html):
    return BeautifulSoup(html, "html.parser")


html = get_election_results(url)
soup = parse_election_results(html)


print(soup.title)



