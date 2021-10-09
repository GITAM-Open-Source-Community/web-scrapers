import requests

head =  {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
    }

def get_youtube_music_results(query):
    query = query.replace(' ','+')
    response = requests.get("https://music.youtube.com/search?q="+query, headers=head).text
    jsonString = response.split("JSON.parse('\\x7b\\x22query\\x22")[1].split("data:")[1].split("'")[1]
    replace = jsonString.replace("\\x22","\"")
    results = replace.split("musicShelfRenderer")
    top_results =[]
    for i in results:
        try:
            category = i.split("text\"")[1].split("\"")[1]
            type = i.split("\"musicVideoType\"")[1].split("\"")[1]
            videoId = i.split("\"videoId\"")[1].split("\"")[1]
            link = "https://music.youtube.com/watch?v="+videoId
            top_results.append((category, type, videoId, link),)
        except: pass
    return top_results

result = get_youtube_music_results('stay')
print(result)