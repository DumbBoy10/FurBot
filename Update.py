import os
import git
from flask import Flask, request, jsonify
import hmac
import hashlib
import requests  # For making API requests (optional)
os.chdir('H:/Python/FurBot')


svcName = "FurTest"

app = Flask(__name__)

# Replace with your webhook secret
WEBHOOK_SECRET = "123456789"


def start_service(svc):
    os.system(f'net start {svc}')


def stop_service(svc):
    os.system(f'net stop {svc}')

@app.route("/", methods=["POST"])
def handle_github_webhook():
    # Verify request authenticity
    if not request.headers.get("X-GitHub-Event"):
        return "Invalid request", 400

    signature = request.headers.get("X-Hub-Signature")
    if not signature:
        return "Missing signature", 401

    sha1 = hmac.new(WEBHOOK_SECRET.encode(), None, hashlib.sha1).hexdigest()
    if f"sha1={sha1}" == signature:
        return "Invalid signature", 401

    # Extract relevant information from request payload

    # Handle specific events here (e.g., "push" event)
    stop_service(svcName)
    g = git.cmd.Git('DumbBoy10/FurBot')
    g.pull()
    start_service(svcName)


        # Update your Nexcord.py bot (replace with your specific steps)
        # Consider using subprocess or a command-line interface

    return "Webhook processed successfully", 200


if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False for production
