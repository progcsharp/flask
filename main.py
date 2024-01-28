from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def handle_post_request():
    name = request.form.get('name')
    
    phone = request.form.get('phone')

    # Отправка GET запроса на другой сервис
    response = requests.get('https://crm-myhome.com/rest/1/so6i37j8xwrpjmbq/crm.lead.add.json', params={'fields[NAME]': name, 'fields[PHONE]': phone})

    return response.text

@app.route('/', methods=['GET'])
def handle_get_request():
    return 'sdvsdvsdsdv'

if __name__ == '__main__':
    app.run()