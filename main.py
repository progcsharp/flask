from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def handle_post_request():
    title = request.form.get('title')
    name = request.form.get('name')
    second_name = request.form.get('second_name')
    last_name = request.form.get('last_name')
    status_id = request.form.get('status_id')
    opened = request.form.get('opened')
    assigned_by_id = request.form.get('assigned_by_id')
    currency_id = request.form.get('currency_id')
    opportunity = request.form.get('opportunity')
    phone = request.form.get('phone')
    web = request.form.get('web')

    if name == '' or phone == []:
        return 'Error: Name and phone are required fields'

    params = {
        'fields[TITLE]': title,
        'fields[NAME]': name,
        'fields[SECOND_NAME]': second_name,
        'fields[LAST_NAME]': last_name,
        'fields[STATUS_ID]': status_id,
        'fields[OPENED]': opened,
        'fields[ASSIGNED_BY_ID]': int(assigned_by_id),
        'fields[CURRENCY_ID]': currency_id,
        'fields[OPPORTUNITY]': int(opportunity),
        'fields[PHONE]': int(phone),
        'fields[WEB]': web
    }

    # Отправка GET запроса на другой сервис
    response = requests.get('https://crm-myhome.com/rest/1/so6i37j8xwrpjmbq/crm.lead.add.json',
                            params=params)

    return response.text


@app.route('/', methods=['GET'])
def handle_get_request():
    return 'TEST'


if __name__ == '__main__':
    app.run()
