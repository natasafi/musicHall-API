# MusichallAPI

A python project that fetches lyrics and artists data from an API.

## Installation

If you have not downloaded python do so as per documentation [python](https://www.python.org/downloads/).

```bash
# clone the repository
https://github.com/natasafi/lyricsAPI.git


```
## Available Endpoints
Open your [browser](http://127.0.0.1:5000)
```
EndPoint                | Result
------------------------| -------------
http://127.0.0.1:5000/  | redirects you to a 
                        | lyrics or artist search
------------------------| -------------
------------------------| -------------
http://127.0.0.1:5000/  |  allows you to insert artist name and song
searchLyrics            | 
------------------------| -------------
------------------------| -------------
http://127.0.0.1:5000/  | returns the lyrics of your search or an error 
lyricsResult            | page if there are no lyrics allowing you to 
                        | search again
------------------------| -------------
------------------------| -------------
http://127.0.0.1:5000/  | allows you to search for an artist with their
searchArtistData        | name
------------------------| -------------
------------------------| -------------
http://127.0.0.1:5000/  | returns the id and type of the artist
artistID                | 
------------------------| -------------

```

## Tech Used
* Python 3.9 : main programming language

* Flask 1.12 : main framework

* venv: virtual environment for running python

* unittest : testing framework

* HTML5: markup language to present responses on the browser

* PyCharm : IDE

## TPAPIs
[musicbrainz](https://musicbrainz.org/doc/MusicBrainz_API)

[lyricsovh](https://lyricsovh.docs.apiary.io/#)

## Author
Natasa Fragkou