from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


class HabraHandler(BaseHTTPRequestHandler):

    HABRA_DOMAIN = 'habrahabr.ru'
    TM_SYMBOL = "\u2122"

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=UTF-8')
        self.end_headers()

        html = self.get_habra_page()
        html = self.get_tm_page(html)
        html = self.sub_anchors(html)
        self.wfile.write(html)

    def get_habra_page(self):
        url = "https://{0}{1}".format(self.HABRA_DOMAIN, self.path)
        response = urlopen(url)
        text = response.read()
        return text

    def get_tm_page(self, html):
        """
        Substitution TM symbol in html and return him
        :param html:
        :return:
        """
        soup = BeautifulSoup(html)
        for item in soup.findAll(text=True):
            if self.is_visible(item):
                insert = r"\1{0}".format(self.TM_SYMBOL)
                tm_text = re.sub(r"(?<!-)\b(\w{6})\b(?!-)", insert, item, flags=re.UNICODE)
                if tm_text != item:
                    item.replaceWith(tm_text)

        tm_html = soup.prettify(soup.original_encoding)
        return tm_html

    def sub_anchors(self, html):
        """
        Substitution of references
        :param html:
        :return:
        """
        new_url = "http://{0}:{1}".format(self.server.server_address[0], str(self.server.server_address[1]))
        current_url = "https://{0}".format(self.HABRA_DOMAIN)

        soup = BeautifulSoup(html)
        for a in soup.findAll('a'):
            try:
                a['href'] = a['href'].replace(current_url, new_url)
            except KeyError:
                pass

        tm_html = soup.prettify(soup.original_encoding)
        return tm_html

    @staticmethod
    def is_visible(element):
        """
        Returns true, if the text - displayed
        :param element:
        :return:
        """
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title'] or element == '\n':
            return False
        elif re.match('<!--.*-->', str(element)):
            return False
        return True


HOST_NAME = '127.0.0.1'
PORT_NUMBER = 8050

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), HabraHandler)
    print('Starting server.')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server is stopped.")