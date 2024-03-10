from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    html_beginning = ('<HTML>'
                      '<HEAD><TITLE>Test żądania HTTP</TITLE></HEAD>'
                      '<BODY>')
    html_ending = ('</BODY>'
                   '</HTML>')
    html_contents = (f'<H1>Metoda żądania: {request.method}</H1>'
                     '<TABLE BORDER="1" CELLPADDING="5">'
                     '<TR><TH>Nagłówek HTTP</TH><TH>Wartość</TH>')
    html_contents += ''.join([f'<TR><TD>{header_name}</TD><TD>{header_value}</TD></TR>'
                              for header_name, header_value in request.headers.items()])
    html_contents += '</TABLE>'

    return html_beginning + html_contents + html_ending


if __name__ == '__main__':
    app.run()
