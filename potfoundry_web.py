from flask import Flask, render_template, request, send_file
from models.planters import generate_planter
import os
from datetime import datetime
import logging
import sys

# --- Setup ---
EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

app = Flask(__name__)

# --- Logging to stdout ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
log = logging.getLogger("potfoundry")
flask_log = logging.getLogger("werkzeug")
flask_log.setLevel(logging.INFO)
flask_log.addHandler(logging.StreamHandler(sys.stdout))

log.info("🚀 PotFoundry web server starting...")

@app.before_request
def log_request_info():
    log.info(f"📥 Incoming request: {request.method} {request.path}")

@app.route("/", methods=["GET"])
def index():
    log.info("🔍 Rendering index page")
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    shape = request.form.get("shape", "tapered")
    diameter_top = float(request.form.get("diameter_top", 120))
    diameter_bottom = float(request.form.get("diameter_bottom", 100))
    height = float(request.form.get("height", 150))
    thickness = float(request.form.get("thickness", 4))

    filename = f"planter_{shape}_{diameter_top}x{diameter_bottom}x{height}_{datetime.now().strftime('%Y%m%d%H%M%S')}.stl"
    filepath = os.path.join(EXPORT_DIR, filename)

    log.info(f"🛠 Generating planter with:")
    log.info(f"   • Shape: {shape}")
    log.info(f"   • Top Diameter: {diameter_top} mm")
    log.info(f"   • Bottom Diameter: {diameter_bottom} mm")
    log.info(f"   • Height: {height} mm")
    log.info(f"   • Thickness: {thickness} mm")
    log.info(f"📁 Export path: {filepath}")

    generate_planter(filepath, diameter_top, diameter_bottom, height, thickness)

    log.info("✅ STL file generated successfully")
    return send_file(filepath, as_attachment=True)

# --- Run ---
if __name__ == "__main__":
    log.info("🌐 Running on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)