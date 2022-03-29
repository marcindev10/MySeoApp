from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return  render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
