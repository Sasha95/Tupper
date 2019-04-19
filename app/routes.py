import base64
import os
from io import BytesIO

from PIL import Image
from flask import render_template, request
from app import app
from app.scripts.degenerate import generate_image
from app.scripts.generate import get_image
MAX_FILE_SIZE = 1024 * 1024 + 1
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

@app.route('/toK', methods=["POST"])
def toK():
    file = request.files["file"]

    k, img = generate_image(file)

    output = BytesIO()
    img.save(output, "PNG")
    contents = base64.b64encode(output.getvalue()).decode()
    output.close()
    contents = contents.split('\n')[0]

    return render_template("degenerate.html", k=k, contents=contents)


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

