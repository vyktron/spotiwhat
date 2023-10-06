from flask import Flask, render_template
import os 


template_path = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=template_path)


@app.route('/')
def index():
    title = "SpotiWHAAAAAAAAAAAAAAAT"
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)