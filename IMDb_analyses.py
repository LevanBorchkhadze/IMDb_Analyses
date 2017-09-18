import urllib.request, json
with urllib.request.urlopen("http://www.myapifilms.com/imdb/"
                            "top?start=1&end=250&token=5a884c79-e016-42a2-aeba-"
                            "29d4245c0e09&format=json&data=1") as url:
    top_250 = json.loads(url.read().decode())
    print(top_250)

with urllib.request.urlopen("http://www.myapifilms.com/imdb/"
                            "bottom?start=1&end=100&token=5a884c79-e016-42a2-aeba-"
                            "29d4245c0e09&format=json&data=1") as url:
    bottom_100 = json.loads(url.read().decode())
    print(bottom_100)