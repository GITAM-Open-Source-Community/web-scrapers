from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
from pydantic import BaseModel


class Post(BaseModel):
    title: str = ""
    author: str = ""
    url: str = ""
    date: str = ""


class DevToScrap:
    def __init__(self, url):
        self.url_page = url
        self.posts = []

    def _find_posts(self):
        page = requests.get(self.url_page)
        soup = BeautifulSoup(page.content, "html.parser")
        home = soup.find(class_="articles-list crayons-layout__content")
        self.posts_array = home.find_all(class_="crayons-story")

    def _format_date(self, raw_post):
        raw_date = raw_post.find("a", class_="crayons-story__tertiary fs-xs").text
        new_date = (
            f"{raw_date} 21"
            if len(raw_date.split(" ")) <= 2
            else raw_date.replace("'", "")
        )
        new_date = datetime.strptime(new_date, "%b %d %y").date()
        self.date = new_date.strftime("%d-%m-%Y")

    def _get_author(self, raw_post):
        author = raw_post.find("div", class_="crayons-story__meta")
        self.author = author.find("button").text.strip()

    def _get_url(self, raw_url):
        href = raw_url.find("a")["href"]
        self.url_post = f"https://dev.to{href}"

    def _get_title(self, raw_title):
        self.title = raw_title.text.strip()

    def _export_to_json(self, data):
        with open("posts.json", "w") as outfile:
            json.dump(data, outfile)

    def run_scrap(self):

        self._find_posts()

        for post in self.posts_array:
            title_link = post.find("h2", class_="crayons-story__title")
            self._get_title(title_link)
            self._get_url(title_link)
            self._get_author(post)
            self._format_date(post)

            post_info = Post(
                title=self.title, author=self.author, url=self.url_post, date=self.date
            )
            self.posts.append(post_info.dict())

        self._export_to_json(self.posts)


if __name__ == "__main__":
    DevToScrap(url="https://dev.to/top/week").run_scrap()
