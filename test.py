import unittest

import requests

from flask import Flask
from nose.tools import assert_true

app = Flask(__name__)


class FlaskTest(unittest.TestCase):
    # added static methods to simplify the tests and remove the need to implicitly pass the self argument referring
    # to the instance of the class

    @staticmethod
    def test_request_response_index():
        # Send a request to the API server and store the response.
        response = requests.get('http://127.0.0.1:5000/')

        assert_true(response.ok)

    @staticmethod
    def test_request_response_searchLyrics():
        # Send a request to the API server and store the response.
        response = requests.get('http://127.0.0.1:5000/searchLyrics')

        assert_true(response.content)

    @staticmethod
    def test_request_response_searchArtistData():
        # Send a request to the API server and store the response.
        response = requests.get('http://127.0.0.1:5000/searchArtistData')

        assert_true(response.content)

    @staticmethod
    def test_request_response_lyricsResult():
        # Send a request to the API server and store the response.
        response = requests.get('http://127.0.0.1:5000/lyricsResult')

        assert_true(response.content)

    @staticmethod
    def test_request_response_artistId():
        # Send a request to the API server and store the response.
        response = requests.get('http://127.0.0.1:5000/artistId')

        assert_true(response.content)


if __name__ == "__main__":
    unittest.main()
