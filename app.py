from flask import Flask
from html.parser import HTMLParser
import requests
url = "https://www.adac.de/verkehr/tanken-kraftstoff-antrieb/kraftstoffpreise/details"
app = Flask(__name__)


def tryParse(value):
    try:
        return float(value), True
    except ValueError:
        return value, False


class AdacHTMLParser(HTMLParser):
    preisDiesel = 0.0
    preisE10 = 0.0
    preisSuper = 0.0

    def handle_data(self, data):
        value, success = tryParse(data.replace(',', '.'))
        if (success):
            if not self.preisDiesel:
                self.preisDiesel = value
            elif not self.preisE10:
                self.preisE10 = value
            elif not self.preisSuper:
                self.preisSuper = value


@app.route('/')
def getRoot():
    r = requests.get(url + "/52070-aachen-sb/2041580621/")
    parser = AdacHTMLParser()
    parser.feed(r.text)
    return {'super': parser.preisSuper, 'e10': parser.preisE10, 'diesel': parser.preisDiesel}


@app.route('/details/<path:path>')
def getDetails(path):
    r = requests.get(url + "/" + path)
    parser = AdacHTMLParser()
    parser.feed(r.text)
    return {'super': parser.preisSuper, 'e10': parser.preisE10, 'diesel': parser.preisDiesel}
