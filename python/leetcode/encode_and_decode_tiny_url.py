import random
import string
from urllib.parse import urlparse


class Codec:

    def __init__(self):
        self.map_long_url_to_short = {}
        self.map_short_url_to_long = {}

    def get_short_url(self):
        characters = string.ascii_lowercase + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(8))

        return short_url

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        shorted_uri = None
        while not shorted_uri:
            shorted_uri = self.get_short_url()
            if shorted_uri in self.map_short_url_to_long:
                shorted_uri = None

        obj = urlparse(longUrl)
        new_url = longUrl.replace(obj.path, f"/{shorted_uri}")
        self.map_long_url_to_short[longUrl] = new_url
        self.map_short_url_to_long[new_url] = longUrl

        return self.map_long_url_to_short[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return self.map_short_url_to_long[shortUrl]


if __name__ == "__main__":
    obj = Codec()

    long_url = 'https://leetcode.com/problems/design-tinyurl'
    assert obj.encode(long_url) == obj.map_long_url_to_short[long_url]
    assert obj.decode(obj.map_long_url_to_short[long_url]) == long_url
