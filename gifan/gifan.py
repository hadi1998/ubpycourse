from flask import Flask, render_template, request

from typing import Optional
import os
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        #f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        a = HTTPBasicAuth('acc_a6e414c2def66d3', 'c733c7e47c5c30bccf63e9d3a877c56f')

        fs = {'image': open(f.filename, 'rb')}
        url = 'https://api.imagga.com/v2/uploads'
        r = requests.post(url, files=fs, auth=a)

        id = r.json()['result']['upload_id']

        p = {'image_upload_id': id}
        url = 'https://api.imagga.com/v2/tags'
        r = requests.get(url, params=p, auth=a)
        j = r.json()

        c = j['result']['tags'][0]['tag']['en'];

        c = requests.get('http://api.giphy.com/v1/gifs/search',params={'q': c, 'api_key': 'cZqNPeXQGNAfukkf8an39bQME0vFB9BY'})
        c = c.json()
        c = c['data']
        list = []
        for i in range(0, 5):
            result = c[i]
            result = result['images']['fixed_height']['url']
            list.append(result)
        addresses = tuple(list)
        return render_template('gifs.html', resp=addresses)
        #print(c)
        #return c



if __name__ == '__main__':
    app.run(debug=True)