import os
import uuid

from flask import Flask, request, abort, flash, jsonify
from subprocess import check_output

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route("/", methods=["POST"])
def get_plate_number():
    if "file" not in request.files:
        flash("No file part")
        return abort(400)
    filename = str(uuid.uuid4()) + ".jpg"
    path_join = os.path.join("/tmp", filename)

    multipart_file = request.files["file"]
    multipart_file.save(path_join)

    try:
        results = check_output(["alpr", "-j", path_join]).decode("utf-8")
        os.remove(path_join)
        return jsonify(results), 200
    except:
        results = check_output(["alpr", "-j", "empty.jpg"]).decode("utf-8")
        os.remove(path_join)
        return jsonify(results), 206


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
