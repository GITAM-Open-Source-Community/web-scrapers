# Web Scraper to get top week reviews from letterboxd

To get started run :
```bash
  pip install -r requirements.txt
```
And run the main file using :
```bash
  python main.py
``` 
So the output is a json file 'comments.json' with the format:
| Parameter    | Type     | Description      |
| :----------- | :------- | :--------------- |
| `film_title` | `string` | title of film    |
| `author`     | `string` | author of review |
| `url`        | `string` | url of review    |
| `date`       | `string` | date of review   |
| `comment`    | `string` | review of film   |