from bs4 import BeautifulSoup
import html5lib
import requests
import json
url = 'https://www.huffingtonpost.fr/'
def get_url_if_not_none(e):
    if e:
        return e.text.strip()
    return None

def get_all_url(url):
    if url:   
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        data = []
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html5lib')
            section = soup.find("section", class_="newsUne")
            links = section.find_all('a')
            div_horizontal = soup.find("div", class_='horizontalCardImg')
            links2 = div_horizontal.find_all("a")
            for link in links:
                data.append(link.get('href'))
            for link in links2:
                data.append(link.get('href'))
            with open("links.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return data
    return None

get_all_url(url)

def get_data():
    json_root = 'links.json'
    with open(json_root, "r", encoding='utf-8') as f:
        all_link = json.load(f)
    return all_link

print(len(get_data()))
