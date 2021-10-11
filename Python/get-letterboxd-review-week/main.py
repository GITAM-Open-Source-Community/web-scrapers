from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
from pydantic import BaseModel


class Review(BaseModel):
    film_title: str = ""
    author: str = ""
    url: str = ""
    date: str = ""
    comment: str = ""


class DevToScrap:
    def __init__(self, url):
        self.url_page = url
        self.reviews = []

    def _find_reviews(self):
        page = requests.get(self.url_page)
        soup = BeautifulSoup(page.content, "html.parser")
        home = soup.find(class_="site-body")
        self.review_array = home.find_all(class_="film-detail")

    def _format_date(self, raw_post):
        raw_date = raw_post.find("span", class_="_nobr").text
        if len(raw_date) == 0:
            raw_date = raw_post.find("time")["datetime"]
            new_date = datetime.strptime(raw_date.split("T")[0], "%Y-%m-%d").date()
            self.date = new_date.strftime("%d-%m-%Y")
            return
        new_date = datetime.strptime(raw_date, "%d %b %Y").date()
        self.date = new_date.strftime("%d-%m-%Y")

    def _get_author(self, raw_post):
        author = raw_post.find("strong", class_="name")
        self.author = author.text.strip()

    def _get_url(self, raw_url):
        href = raw_url.find("a")["href"]
        self.url_review = f"https://letterboxd.com{href}"

    def _get_title(self, review_block):
        self.title = review_block.text[:-4].strip()

    def _get_comment(self, review_block):
        comment = review_block.find(class_="body-text -prose collapsible-text").text
        self.comment = comment.replace(
            "This review may contain spoilers. I can handle the truth.  ", ""
        )

    def _export_to_json(self, data):
        with open("comments.json", "w") as outfile:
            json.dump(data, outfile)

    def run_scrap(self):

        self._find_reviews()

        for review in self.review_array:
            review_block = review.find(class_="film-detail-content")
            title_block = review_block.find(class_="headline-2 prettify")
            self._get_title(title_block)
            self._get_url(title_block)
            self._get_author(review)
            self._format_date(review)
            self._get_comment(review_block)

            post_info = Review(
                film_title=self.title,
                author=self.author,
                url=self.url_review,
                date=self.date,
                comment=self.comment,
            )
            self.reviews.append(post_info.dict())

        self._export_to_json(self.reviews)


if __name__ == "__main__":
    DevToScrap(url="https://letterboxd.com/reviews/popular/this/week/").run_scrap()
