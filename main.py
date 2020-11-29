import json

import requests
from flask import Flask, render_template, request

app = Flask(__name__)


# landing page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# lets you insert artist and song for lyrics search
@app.route("/searchLyrics", methods=['GET'])
def get_lyrics():
    return render_template('lyricsSearch.html')


# lets you insert artist for id search
@app.route("/searchArtistData", methods=['GET'])
def get_artist_data():
    return render_template('artistSearch.html')


# presents the lyrics from the search or an error page if no lyrics
@app.route("/lyricsResult", methods=['POST'])
def request_lyrics():
    artist = request.form.get("artist")
    title = request.form.get("song")
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    res = requests.get(url)

    if res.status_code != 200:
        print(res.text)
        return None
    else:
        lyrics = json.loads(res.text)['lyrics']
        print(lyrics)
        if len(lyrics) >= 1:
            return render_template('lyricsResults.html', artist=artist, title=title, lyrics=lyrics)
        else:
            # for certain searches I was getting no lyrics sometimes. Thought to be good to add a warning since I
            # spotted it.
            return render_template('empty.html')


# presents the artist ID from the search
@app.route("/artistId", methods=['POST'])
def request_artist_id():
    artist = request.form.get("artist")
    url = f"https://musicbrainz.org/ws/2/artist?query={artist}&fmt=json"
    res = requests.get(url)
    if res.status_code != 200:
        print(res.text)
        return None
    else:
        jsonData: dict = json.loads(res.text)
        jsonId = jsonData['artists'][0]['id']
        jsonType = jsonData['artists'][0]['type']

        # didn't manage to find a proper way to map the values of the json response to a dic with a for loop (－‸ლ)
        info = {'id': jsonId, 'type': jsonType}
        print(info)

        return render_template('artistResults.html', artist=artist, info=info)


app.run(debug=True)
