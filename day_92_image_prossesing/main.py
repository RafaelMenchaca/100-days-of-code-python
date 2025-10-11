from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import numpy as np
import os
import collections

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

def rgb_to_hex(rgb_tuple):
    return "#{:02x}{:02x}{:02x}".format(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])

def get_top_colors(image_path, num_colors=10):
    # Open image with PIL
    img = Image.open(image_path).convert("RGB")
    # Optionally resize to speed up
    img = img.resize((300, 300))
    arr = np.array(img)
    # Reshape: (height * width, 3)
    pixels = arr.reshape(-1, 3)
    # Count each RGB triple
    counter = collections.Counter(map(tuple, pixels))
    most_common = counter.most_common(num_colors)
    # Return list of (hex, count)
    result = [(rgb_to_hex(rgb), count) for rgb, count in most_common]
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image_file")
        if not file:
            return redirect(request.url)
        filename = file.filename
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(path)
        top_colors = get_top_colors(path, num_colors=10)
        return render_template("index.html", palette=top_colors, image_url=path)
    return render_template("index.html", palette=None)

if __name__ == "__main__":
    app.run(debug=True)
