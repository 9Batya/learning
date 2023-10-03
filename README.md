from flask import Flask, request

app = Flask(__name__)

@app.route('/event/api/v0/event/json/1695892203ZNC972', methods=['POST'])
def analyze():
    request_data = request.get_json()
    print(request_data)

    ip_address = request.remote_addr
    print("IP адрес: ", ip_address)

    return 'Анализ выполнен успешно'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
