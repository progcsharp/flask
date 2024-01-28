from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def handle_post_request():
    data = request.form
    if data.get("test"):
        return "test"
    name = data.get("name")
    phone = data.get("phone")

    try:
        params = {
            'fields[NAME]': name,
            'fields[PHONE]': phone
        }
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    try:
        link = f'https://webhook.site/b50e3fbc-129b-4076-a869-de0669d2d3aa'
        print(link)
        response = requests.get(link, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

    return "ok"


@app.route('/', methods=['GET'])
def handle_get_request():
    return 'The server is working correctly'


if __name__ == '__main__':
    app.run(port=1234)
