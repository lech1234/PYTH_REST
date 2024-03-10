from flask import Flask

app = Flask(__name__)

@app.route('/calc/<dzialanie>/<int:x>/<int:y>', methods=['GET'])
def oblicz(dzialanie, x, y):
    match dzialanie:
        case 'dodaj': return str(x + y)
        case 'odejmij': return str(x - y)
        case 'pomnoz': return str(x * y)
        case 'podziel': return str(x / y)

if __name__ == '__main__':
    app.run()