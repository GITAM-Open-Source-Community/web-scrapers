# Web Scraper to get top news from hltv.org

To get started run :
```bash
  pip install -r requirements.txt
```
And run the main file using :
```bash
  python main.py
``` 
So the output is a json file 'news.json' with the format:
| Parameter | Type     | Description    |
| :-------- | :------- | :------------- |
| `title`   | `string` | title of news  |
| `region`  | `string` | region of news |
| `url`     | `string` | url of news    |
| `date`    | `string` | date of news   |