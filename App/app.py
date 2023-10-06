from flask import Flask, render_template, request
import os

template_path = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=template_path)

# Liste de noms de boutons
button_names = ['Rap', 'Pop', 'Reggae', 'Rock', 'Mix Aléatoire']

X=['1','2']
L1 = [X, 'b', 'c', 'd', 'e']
L2 = ['f', 'g', 'h', 'i', 'j']
L3 = ['k', 'l', 'm', 'n', 'o']
L4 = ['p', 'q', 'r', 's', 't']
L5 = ['u', 'v', 'w', 'x', 'y']

@app.route('/')
def index():
    title = "SpotiWHAAAAAAAAAAAAAAAT"
    return render_template('index.html', title=title, button_names=button_names, selected_list=None)

@app.route('/show_list', methods=['POST'])
def show_list():
    button_name = request.form.get('button_name')
    selected_list = get_list_for_button(button_name)
    title = "List " + button_name
    return render_template('index.html', title=title, button_names=button_names, selected_list=selected_list)

def get_list_for_button(button_name):
    if button_name == 'Rap':
        return L1
    elif button_name == 'Pop':
        return L2
    elif button_name == 'Reggae':
        return L3
    elif button_name == 'Rock':
        return L4
    elif button_name == 'Mix Aléatoire':
        return L5

if __name__ == '__main__':
    app.run(debug=True)
