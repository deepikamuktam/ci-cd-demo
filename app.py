from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD Pipeline with GitHub Actions & Docker!"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
