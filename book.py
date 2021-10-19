import requests
import parsel


"""
::text 提取文字
::attr() 提取指定属性

"""

if "__main__" == __name__:
    content_url = "https://www.shuquge.com/txt/8072/24391986.html"
    response = requests.get(content_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'})
    response.encoding = 'utf-8'
    sel = parsel.Selector(response.text)
    title = sel.css('.reader h1::text').getall()  # 得到列表
    content = sel.css('.showtxt::text').getall()
    with open(title[0]+'.txt', mode='w', encoding='utf-8') as f:
        f.write(title[0]+'\r\n')
        for c in content:
            f.write(c.strip())
