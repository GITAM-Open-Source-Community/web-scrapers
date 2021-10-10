# Web Scraper to get top week posts from dev.to

To get started run :
```bash
  pip install -r requirements.txt
```
And run the main file using :
```bash
  python main.py
``` 
So the output is a json file 'posts.json' with the format:
| Parameter | Type     | Description    |
| :-------- | :------- | :------------- |
| `title`   | `string` | title of post  |
| `author`  | `string` | author of post |
| `url`     | `string` | url of post    |
| `date`    | `string` | date of post   |