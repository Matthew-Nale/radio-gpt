from flask import Blueprint, request, jsonify
import requests, json

api = Blueprint("api", __name__)

@api.route("/api/generate", methods=["POST"])
def chat():
    data = request.get_json()
    query = {
        'model': 'BaseModel',
        'messages': data["messages"]
    }

    r = requests.post(
        'http://127.0.0.1:8080/chat/completions',
        data=json.dumps(query),
        headers={'Content-Type': 'application/json'}
    )
    r = json.loads(r.content)
    
    data_to_return = {
        'created': r["created"],
        'usage': r["usage"],
        'message': r["choices"][0]["message"]["content"]
    }
    return jsonify(data_to_return)