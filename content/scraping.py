from bs4 import BeautifulSoup
import html5lib
import requests
import json
url = 'https://www.huffingtonpost.fr/'
def get_url_if_not_none(e):
    if e:
        return e.text
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
            all_link = {}
            all_link2 = {}
            for index, link in enumerate(links2):
                all_link2[f"linkhorizontal{index+1}"] = link.get('href')

            for index ,link in enumerate(links):
                all_link[f"link{index+1}"] = link.get('href')

            data.append(all_link)
            data.append(all_link2)
            with open("links.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return data
    return None
get_all_url(url)
def get_content_for_article():
    json_root = 'links.json'
    with open(json_root, "r", encoding='utf-8') as f:
        all_link = json.load(f)
    return all_link

print(get_content_for_article()[0],"************************")

def run():
    pass