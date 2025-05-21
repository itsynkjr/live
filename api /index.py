from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Music WRLD Backend Running!"

@app.route("/api/mix-master", methods=["POST"])
def mix_master():
    vocal = request.files.get("vocal")
    instrumental = request.files.get("instrumental")

    if not vocal or not instrumental:
        return jsonify({"error": "Both vocal and instrumental files are required"}), 400

    # Just return success message for now
    return jsonify({"message": "Files received. Mixing will be added soon."}), 200

@app.route("/api/generate-lyrics", methods=["GET"])
def generate_lyrics():
    return jsonify({
        "lyrics": "Yo, I came from the bottom, now I’m rising above. Life hit me hard, but I fight with love..."
    })

@app.route("/api/create-beat", methods=["GET"])
def create_beat():
    return jsonify({
        "message": "Beat generation coming soon."
    })

if __name__ == "__main__":
    app.run(debug=True)
