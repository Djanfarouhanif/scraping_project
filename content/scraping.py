from bs4 import BeautifulSoup
import html5lib
import requests
import json
url = 'https://www.huffingtonpost.fr/'
def get_url_if_not_none(e):
    if e:
        return e.text.strip()
    return None
#===================recuperations des url des article ============================
def get_all_url(url):
    if url:   
        try:
            response = requests.get(url)
            response.encoding = response.apparent_encoding
        except:
            return None
        Links = []
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html5lib')
            section = soup.find("section", class_="newsUne")
            links = section.find_all('a')
            div_horizontal = soup.find("div", class_='horizontalCardImg')
            links2 = div_horizontal.find_all("a")
            for link in links:
                Links.append(link.get('href'))
            for link in links2:
                Links.append(link.get('href'))
            # with open("links.json", "w", encoding="utf-8") as f:
            #     json.dump(data, f, ensure_ascii=False, indent=4)
            return Links
    return None
#=============fonction pour lencer la recuperations des article===================
def run():
    Links = get_all_url(url)
    return Links
#==================Lecture des fichier=====================
# def get_data():
#     try:
#         json_root = 'links.json'
#         with open(json_root, "r", encoding='utf-8') as f:
#             all_link = json.load(f)
#         return all_link
#     except:
#         return None
