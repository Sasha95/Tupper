import os
from flask import render_template, request
from app import app
from app.scripts.degenerate import generate_image
from app.scripts.generate import get_image

# https://habrastorage.org/getpro/habr/post_images/b3c/587/908/b3c5879085ad90e7bdb51854803b2375.png
@app.route('/')
def main():
       return render_template('index.html')

@app.route('/toK')
def toK_form():
    filePath = "app/static/result.png"
    if os.path.exists(filePath):
        os.remove(filePath)

    return render_template('degenerate.html')

@app.route('/toK', methods=['POST'])
def toK():
    text = request.form['text']
    k = generate_image(text)
    return render_template('degenerate.html', k=k, image=text)

@app.route('/fromK')
def fromK_form():
    filePath = "app/static/image.png"
    if os.path.exists(filePath):
        os.remove(filePath)
    return render_template('generate.html')

@app.route('/fromK', methods=['POST'])
def fromK():
    text = str(request.form['text']).strip().replace(' ', '')
    contents = get_image(int(text))
    return render_template('generate.html', contents=contents)

