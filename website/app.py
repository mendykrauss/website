from flask import Flask, redirect, request, Response, render_template

app = Flask(__name__, template_folder='mk-website/templates', static_folder='mk-website/css')

@app.route('/')
def index():
    return render_template('page.html')


@app.route('/favicon.ico')
def favicon():
    res = Response(status=200, mimetype='image/png')
    return res


if __name__ == '__main__':
    app.run(port=3216, debug=True)