from flask import Flask, render_template, request, send_file
from models.planters import generate_planter
import os
from datetime import datetime

app = Flask(__name__)
EXPORT_DIR = "exports"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    shape = request.form.get("shape", "tapered")
    diameter_top = float(request.form.get("diameter_top", 120))
    diameter_bottom = float(request.form.get("diameter_bottom", 100))
    height = float(request.form.get("height", 150))
    thickness = float(request.form.get("thickness", 4))

    filename = f"planter_{datetime.now().strftime('%Y%m%d%H%M%S')}.stl"
    filepath = os.path.join(EXPORT_DIR, filename)

    generate_planter(filepath, diameter_top, diameter_bottom, height, thickness)
    return send_file(filepath, as_attachment=True)
