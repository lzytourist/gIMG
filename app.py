from flask import Flask, render_template, request, send_from_directory, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("index.html")


@app.route('/crawl', methods=["POST", "GET"])
def crawl():
    if request.method == "POST":
        website = request.form.get("website")
        if not website:
            return jsonify({
                'status': False,
                'message': 'Please provide a website link!'
            })

        image_links = []
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/94.0.4606.71 Safari/537.36',
            }
            html = requests.get(website, headers=headers).text
            soup = BeautifulSoup(html, 'html.parser')
            images = soup.find_all('img')
            for image in images:
                link = image.get('src')
                if not link:
                    link = image.get('data-src')
                if type(link) == "str" and 'http' not in link:
                    link = website + '/' + link

                image_links.append(link)
        except requests.exceptions.MissingSchema as e:
            return jsonify({
                'status': False,
                'message': 'Could not load website.'
            })

        return jsonify({
            'status': True,
            'message': 'Website loaded!',
            'images': image_links
        })
    return "HI CHOTTO BONDHU!"


if __name__ == '__main__':
    app.debug = True
    app.run()
