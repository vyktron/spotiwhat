from flask import Flask, render_template, request
import playground as pg
import os

template_path = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=template_path)

# Liste de noms de boutons
button_names = ['Rap', 'Pop', 'Electro', 'Rock', 'Country']

@app.route('/')
def index():
    title = "SpotiWHAAAAAAAAAAAAAAAT"
    return render_template('index.html', title=title, button_names=button_names, selected_list=None)

@app.route('/show_list', methods=['POST'])
def show_list():
    button_name = request.form.get('button_name')
    selected_list = get_list_for_button(button_name)
    title = "SpotiWHAAAAAAAAAAAAAAAT"
    liste_name="List " + button_name
    return render_template('index.html', title=title, liste_name=liste_name, button_names=button_names, selected_list=selected_list)

def get_list_for_button(button_name : str):
    infos, danceability, length = pg.front_infos(pg.get_playlist_from_genre(button_name.lower(), 5))
    return infos

if __name__ == '__main__':
    app.run(debug=True)
