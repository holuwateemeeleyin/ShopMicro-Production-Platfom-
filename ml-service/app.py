from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "ml-service"})

@app.route("/recommendations/<int:user_id>", methods=["GET"])
def recommendations(user_id):
    catalog = ["keyboard", "monitor", "headset", "mouse", "webcam"]
    random.seed(user_id)
    picks = random.sample(catalog, 3)
    return jsonify({"user_id": user_id, "recommendations": picks})

# --- ADD THIS: The Debugger ---
@app.errorhandler(404)
def resource_not_found(e):
    # This will log the EXACT path that failed to your 'kubectl logs'
    print(f"DEBUG: 404 Error on path: {request.path}")
    return jsonify(error=str(e), path=request.path), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)