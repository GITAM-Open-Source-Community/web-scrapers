# Web Scraper to get top tier matches of the day from hltv.org

To get started run :
```bash
  pip install -r requirements.txt
```
And run the main file using :
```bash
  python main.py
``` 
So the output is a json file 'matches.json' with the format:
| Parameter | Type     | Description     |
| :-------- | :------- | :-------------- |
| `teamA`   | `string` | Team A of match |
| `teamB`   | `string` | Team B of match |
| `event`   | `string` | event of match  |
| `url`     | `string` | url of match    |
| `date`    | `string` | date of match   |