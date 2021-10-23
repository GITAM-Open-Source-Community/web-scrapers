from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
from pydantic import BaseModel
import itertools


class Match(BaseModel):
    teamA: str = ""
    teamB: str = ""
    event: str = ""
    url: str = ""
    date: str = ""


class DevToScrap:
    def __init__(self, url):
        self.url_page = url
        self.matches = []
        self.matches_array = []

    def _find_matches(self):
        page = requests.get(self.url_page)
        soup = BeautifulSoup(page.content, "html.parser")
        home = soup.find(class_="mainContent")
        self.live_matches = home.find(class_="liveMatchesContainer")
        self.upcoming_matches = home.find(class_="upcomingMatchesContainer")

    def _format_date(self, match_block):
        raw_date = match_block.find(class_="matchDayHeadline")
        self.date = raw_date.text

    def _format_time(self, match_block):
        raw_time = match_block.find(class_="matchTime")
        self.time = raw_time.text

    def _get_event(self, matches):
        event = matches.find(class_="matchEventName gtSmartphone-only")
        if event == None:
            event = matches.find(class_="matchInfoEmpty")
        self.event = event.text

    def _get_url(self, raw_url):
        href = raw_url["href"]
        self.url = f"https://www.hltv.org{href}"

    def _get_teams(self, match_block):
        teams = match_block.find_all(class_="matchTeam")
        if teams != []:
            self.teamA = teams[0].text.strip("\n").strip("()").strip()
            self.teamB = teams[1].text.strip("\n").strip("()").strip()
        else:
            self.teamA = "Undefined ?"
            self.teamB = "Undefined ?"

    def _export_to_json(self, data):
        with open("matches.json", "w") as outfile:
            json.dump(data, outfile)

    def run_scrap(self):

        self._find_matches()

        for matches in self.live_matches.find_all(class_="liveMatch-container"):
            self._get_teams(matches)
            self._get_url(matches.find(class_="match a-reset"))
            self._get_event(matches)
            self.date = "LIVE"

            news_info = Match(
                teamA=self.teamA,
                teamB=self.teamB,
                event=self.event,
                url=self.url,
                date=self.date,
            )
            self.matches.append(news_info.dict())

        for matches_block in self.upcoming_matches.find_all(
            class_="upcomingMatchesSection"
        ):
            self._format_date(matches_block)
            for matches in matches_block.find_all(class_="match a-reset"):
                self._get_teams(matches)
                self._get_url(matches)
                self._get_event(matches)
                self._format_time(matches)
                self.full_date = f"{self.date} - {self.time}"

                match_info = Match(
                    teamA=self.teamA,
                    teamB=self.teamB,
                    event=self.event,
                    url=self.url,
                    date=self.full_date,
                )
                self.matches.append(match_info.dict())

        self._export_to_json(self.matches)


if __name__ == "__main__":
    DevToScrap(url="https://www.hltv.org/matches?predefinedFilter=top_tier").run_scrap()
