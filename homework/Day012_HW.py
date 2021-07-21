# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.ettoday.net/news/news-list.htm'
# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html.parser")
# for d in soup.find(class_="part_list_2").find_all('h3'):
#     print(d.find(class_="date").text, d.find_all('a')[-1].text)

import requests
from bs4 import BeautifulSoup

# url = 'https://www.ettoday.net/news/news-list.htm'
# r = requests.get(url)

# soup = BeautifulSoup(r.text, "lxml")
# for d in soup.find(class_="part_list_2").find_all('h3'):
#     print(d.find(class_="date").text, d.find_all('a')[-1].text)


# 抓 title
for tt in [1, 17, 2, 6, 9, 10, 20, 30, 24, 5]:
    title = []
    for n in range(1,11):
        for n2 in [25,10]:
            u = "https://www.ettoday.net/news/news-list-2021-"+str(n)+"-"+str(n2)+"-"+str(tt)+".htm"
            res = requests.get(u)
            soup = BeautifulSoup(res.content, "lxml")
            soup = soup.find("div", class_="part_list_2")
            domian = "https://www.ettoday.net"
            for a in soup.find_all("h3"):
                p = a.a.string
                if p != None:
                    p = p.split('／')
                    if len(p) > 1:
                        title.append(p[1])
                    else:
                        title.append(p[0])

    with open(str(tt)+".txt", "a") as f:
        for t in title:
            f. write(t+"\n")

