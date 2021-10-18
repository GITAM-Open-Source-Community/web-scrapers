from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
from pydantic import BaseModel
import itertools


class News(BaseModel):
    title: str = ""
    region: str = ""
    url: str = ""
    date: str = ""


class DevToScrap:
    def __init__(self, url):
        self.url_page = url
        self.news = []

    def _find_news(self):
        page = requests.get(self.url_page)
        soup = BeautifulSoup(page.content, "html.parser")
        home = soup.find(class_="contentCol")
        news = home.find_all(class_="standard-box standard-list")
        self.news_array = [i.find_all("a") for i in news]
        self.news_array = list(itertools.chain.from_iterable(self.news_array))

    def _format_date(self, news):
        raw_date = news.find(class_="newsrecent")
        self.date = raw_date.text

    def _get_region(self, news):
        region = news.find(class_="newsflag flag")["title"]
        self.region = region

    def _get_url(self, raw_url):
        href = raw_url["href"]
        self.url = f"https://www.hltv.org{href}"

    def _get_title(self, news_block):
        title = news_block.find(class_="newstext")
        self.title = title.text

    def _export_to_json(self, data):
        with open("news.json", "w") as outfile:
            json.dump(data, outfile)

    def run_scrap(self):

        self._find_news()

        for news in self.news_array:
            self._get_title(news)
            self._get_url(news)
            self._get_region(news)
            self._format_date(news)

            news_info = News(
                title=self.title,
                region=self.region,
                url=self.url,
                date=self.date,
            )
            self.news.append(news_info.dict())

        self._export_to_json(self.news)


if __name__ == "__main__":
    DevToScrap(url="https://www.hltv.org/").run_scrap()
