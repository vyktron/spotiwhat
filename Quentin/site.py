from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "Bienvenue sur notre site"
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)