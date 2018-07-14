import re, scrapy, requests
from bs4 import BeautifulSoup
from scrapy.http import Request
from spiderpig.items import NovelItem, ContentItem

class Myspider(scrapy.Spider):
    name = 'biqukan'

    def __init__(self):
        self.target_site = 'http://www.biqukan.com/'
        self.categories = self.category_urls()

    def start_requests(self):
        for url in self.categories:
            yield Request(url, self.parse)

    def parse(self, response):
        print("here is the parse part")

        html_bf = self.__get_html_bf(response)

        # get all story links, we still need to get article link through these
        hrefs = html_bf.find_all(href=re.compile("^\/[0-9_]+\/$"))

        result = set()
        for each in hrefs:
            novel_name = each.get_text()
            #result.add(self.target_site.rstrip('/') + each.get('href'))
            novel_url = self.target_site.rstrip('/') + each.get('href')
            yield Request(novel_url, self.get_novel_info, meta={'url': novel_url})

    def category_urls(self):
        req = requests.get(url = self.target_site)
        div_bf = self.__get_html_bf(req)

        div = div_bf.find('div', class_ = 'nav')
        a_bf = BeautifulSoup(str(div))
        a = a_bf.find_all('a')

        result = set()
        for each in a[2:]:
            result.add(self.target_site.rstrip('/') + each.get('href'))

        return result

    def get_novel_info(self, response):
        print("here is the get novel info part")

        item = NovelItem()
        item['novelurl'] = str(response.meta['url'])
        html_bf = self.__get_html_bf(response)

        novel_info = html_bf.find('div', class_ = 'info')
        novel_small = html_bf.find('div', class_ = 'small')

        spans = novel_small.find_all('span')

        item['name'] = novel_info.find('h2').get_text()
        item['author'] = spans[0].get_text()[3:]
        item['category'] = spans[1].get_text()[3:]
        item['serialstatus'] = spans[2].get_text()[3:]
        item['serialnumber'] = spans[3].get_text()[3:]

        yield item

        chapter_start_tag = html_bf.find_all('dt')[1]
        chapters_info = chapter_start_tag.find_next_siblings('dd')
        chapter_order = 0

        for each in chapters_info:
            chapter_order += 1
            chapter_url = self.target_site.rstrip('/') + each.find('a').get('href')
            yield Request(chapter_url, self.get_chapter_info, meta = {'novelurl': item['novelurl'], 'chapter_order': chapter_order, 'chapter_url': chapter_url})

    def get_chapter_info(self, response):
        novelurl = response.meta['novelurl']
        chapterorder = response.meta['chapter_order']
        chapterurl = response.meta['chapter_url']

        html_bf = self.__get_html_bf(response)

        content = html_bf.find('div', class_ = 'content')

        chaptername = content.find('h1').get_text()
        chaptercontent = content.find('div', id = 'content').get_text()

        item = ContentItem()

        item['novelurl'] = novelurl
        item['chaptercontent'] = chaptercontent
        item['chapterorder'] = chapterorder
        item['chapterurl'] = chapterurl
        item['chaptername'] = chaptername

        yield item

    def __get_html_bf(self, response):
        html = response.text
        html_bf = BeautifulSoup(html, "html.parser")

        return html_bf
