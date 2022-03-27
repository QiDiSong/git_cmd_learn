import requests
import bs4

hd = {'User-Agent': 'Mozilla/5.0'}
res = requests.get("https://movie.douban.com/top250", headers=hd)
res.raise_for_status()
res.encoding = res.apparent_encoding
print(res.headers)
print(res.request.headers)
soup = bs4.BeautifulSoup(res.text, "html.parser")
target = soup.find_all("div", class_="hd")
print(len(res.text))


for each in target:
    print(each.a.span.text)


# url = 'https://movie.douban.com/top250'
#
# hd = {'User-Agent': 'Mozilla/5.0'}
# def get_html_text(url):
#     try:
#         r = requests.get(url, timeout=10, headers=hd)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         html = r.text
#         return html
#     except Exception as result:
#             print('Error Type: ', result)
#
# html = get_html_text(url)
# print(len(html))
# soup = bs4.BeautifulSoup(html, "html.parser")
# target = soup.find_all("div", class_="hd")
# for each in target:
#     print(each.a.span.text)