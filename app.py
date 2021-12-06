from flask import Flask, render_template
import requests, markdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/releases")
def releases():
    info = get_info()
    return render_template('releases.html', name=info["name"], body= markdown.markdown(info["body"]), link=info["link"], release_link=info["release_link"])

def get_info():
    response = requests.get("https://api.github.com/repos/pgamerx/yt-dislikes-viewer/releases/latest")
    return {"name": response.json()["name"], "body": response.json()["body"], "link": response.json()["assets"][0]["browser_download_url"],"release_link": response.json()["url"]}

if __name__ == '__main__':
    app.run(debug=True)