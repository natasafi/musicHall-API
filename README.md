# MusichallAPI

A python project that fetches lyrics and artists data from an API.

## Installation

If you have not downloaded python do so as per documentation [python](https://www.python.org/downloads/).

Check on your terminal by running

```bash
python --version
```
If you have not downloaded docker do so as per [docker](https://www.docker.com/products/docker-desktop)
Then
```bash
# clone the repository
https://github.com/natasafi/lyricsAPI.git

# open it on your favourite IDE
# ensuring that you are on the right path of the project run the following command on your terminal to build the image
docker build -t musichall_api .

# ensure that is being built after the end of the process with
docker ps
# run the Docker image of our app with the following command which will expose it to a port on the browser
 docker run -p 5000:5000 musichall_api
# follow the link and navigate to the following endpoints on the browser

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

* Docker : creates an instance of the app with the relevant dependecies
## TPAPIs
[musicbrainz](https://musicbrainz.org/doc/MusicBrainz_API)

[lyricsovh](https://lyricsovh.docs.apiary.io/#)

## Author
Natasa Fragkou