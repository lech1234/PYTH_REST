from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    html_beginning = ('<HTML>'
                      '<HEAD><TITLE>Test żądania HTTP</TITLE></HEAD>'
                      '<BODY>')
    html_ending = ('</BODY>'
                   '</HTML>')
    html_contents = '<H1>Request method:</H1>' + request.method

    html_contents += '<H1>Request headers:</H1>'
    html_contents += '<BR>'.join([header_name + ': ' + header_value
                                  for header_name, header_value in request.headers.items()])

    return html_beginning + html_contents + html_ending


if __name__ == '__main__':
    app.run()
