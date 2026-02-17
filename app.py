# Telegram STAR GAMER
#DONT CHANGE CREDIT 
#IF YOU CHANGE MY CREDIT, I'LL FUCK YOUR MOM
from flask import Flask, request, jsonify
import requests
import json
import threading
from byte import Encrypt_ID, encrypt_api

app = Flask(__name__)

# Owner: @STAR_rdp

def load_tokens():
    try:
        # Owner: @STAR_RDP
        with open("spam_ind.json", "r") as file:
            data = json.load(file)
        tokens = [item["token"] for item in data]  
        return tokens
    except Exception as e:
        print(f"Error loading tokens: {e}")  # @STAR_RDP
        return []

def send_friend_request(uid, token, results):
    # Owner: @STAR_RDP
    encrypted_id = Encrypt_ID(uid)
    payload = f"08a7c4839f1e10{encrypted_id}1801"
    encrypted_payload = encrypt_api(payload)

    url = "https://client.ind.freefiremobile.com/RequestAddingFriend"
    headers = {
        "Expect": "100-continue",
        "Authorization": f"Bearer {token}",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB52",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "16",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-N975F Build/PI)",
        "Host": "clientbp.ggblueshark.com",
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate, br"
    }

    response = requests.post(url, headers=headers, data=bytes.fromhex(encrypted_payload))

    if response.status_code == 200:
        results["success"] += 1
    else:
        results["failed"] += 1

@app.route("/spam", methods=["GET"])
def spam():
    # API Owner: @STAR_RDP
    uid = request.args.get("uid")
    key = request.args.get("key")
    
    # Key validation by @STAR_RDP
    if key != "STAR":
        return jsonify({
            "error": "Invalid or missing key 🔐",
            "owner": "@STAR_RDP"
        }), 401
    
    if not uid:
        return jsonify({
            "error": "uid parameter is required",
            "owner": "@STAR_RDP"
        }), 400

    tokens = load_tokens()
    if not tokens:
        return jsonify({
            "error": "No tokens found in spam_ind.json",
            "owner": "@STAR_RDP"
        }), 500

    results = {"success": 0, "failed": 0}
    threads = []

    # Sending requests - @STAR_RDP
    for token in tokens[:110]:
        thread = threading.Thread(target=send_friend_request, args=(uid, token, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_requests = results["success"] + results["failed"]
    status = 1 if results["success"] != 0 else 2

    # Response from @STAR_RDP
    return jsonify({
        "success_count": results["success"],
        "failed_count": results["failed"],
        "status": status,
        "owner": "@STAR_RDP",
        "message": "API by @STAR_RDP"
    })

if __name__ == "__main__":
    # Server by @STAR_RDP
    app.run(debug=True, host="0.0.0.0", port=5000)
