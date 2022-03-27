import re
import requests
import bs4

def open_url(url):
    # 使用代理
    hd = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=hd)

    return res

def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # movies name
    movies = []
    targets = soup.find_all("span", class_="hd")
    for each in targets:
        movies.append(each.a.span.text)

    # ranks score
    ranks = []
    targets = soup.find_all("span", class_="rating_num")
    for each in targets:
        ranks.append(" 评分： %s " % each.text)

    # messages
    messages = []
    targets = soup.find_all("div", class_="bd")
    for each in targets:
        try:
            messages.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + ranks[i] + messages[i] + '\n')

    return result

def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text

    return int(depth)

def main():
    host = 'https://movie.douban.com/top250'
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(depth):
        url = host + '/?start=' + str(25 * i)
        res = open_url(url)
        result.extend(find_movies(res))

    with open("doubanTop250.txt", "w", encoding='utf-8') as f:
        for each in result:
            f.write(each)

if __name__ == '__main__':
    main()
    print('success')