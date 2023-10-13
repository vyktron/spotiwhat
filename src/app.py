from flask import Flask, render_template, request
import utils.playground as pg

template_path = 'templates'

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
    selected_list, danceability,energy = get_list_for_button(button_name)
    title = "SpotiWHAAAAAAAAAAAAAAAT"
    liste_name = "List " + button_name

    # Crée des liens YouTube pour chaque élément de la liste
    selected_list_with_links = [(item, f"https://www.youtube.com/results?search_query={item}") for item in selected_list]

    return render_template('index.html', title=title, liste_name=liste_name, button_names=button_names, selected_list=selected_list_with_links,energy=energy,danceability=danceability)

def get_list_for_button(button_name : str):
    infos, danceability, energy, length = pg.front_infos(pg.get_playlist_from_genre(button_name.lower(), 5, pg.DB_NAME, pg.COLL_NAME))
    return infos,danceability,energy

if __name__ == '__main__':

    pg.mongoimport(pg.CSV_PATH, pg.DB_NAME, pg.COLL_NAME)
    app.run(debug=True)

    