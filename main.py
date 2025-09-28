from flask import *
from labyrinthe import Labyrinthe
from tkinter.filedialog import asksaveasfilename

app = Flask(__name__, template_folder="templates")

labyrinthe = None

@app.route('/')
def index():
    return render_template('/index.html', maze=None, solved=False)

@app.route('/generate', methods=['POST'])
def generate():
    global labyrinthe
    width = int(request.form['width'])
    height = int(request.form['height'])
    labyrinthe = Labyrinthe(width, height)
    labyrinthe.generer_fusion()
    texte = labyrinthe.afficher(terminal=False)
    return render_template('index.html', maze=texte, solved=False)

@app.route('/show_answer', methods=['POST'])
def show_answer():
    global labyrinthe
    if labyrinthe:
        labyrinthe.solve()
        texte = labyrinthe.afficher(solved=True, terminal=False)
        return render_template('index.html', maze=texte, solved=True)
    return redirect(url_for('index'))

@app.route('/hide_answer', methods=['POST'])
def hide_answer():
    global labyrinthe
    if labyrinthe:
        texte = labyrinthe.afficher(solved=False, terminal=False)
        return render_template('index.html', maze=texte, solved=False)
    return redirect(url_for('index'))

@app.route('/download', methods=['POST'])
def download():
    global labyrinthe

    if not labyrinthe:
        return redirect(url_for('index'))

    if request.form['download_type'] == 'pdf':
        if request.form['download_content'] == 'maze':
            labyrinthe.generate_pdf(basic=True, with_solved=False)
        elif request.form['download_content'] == 'maze_and_solution':
            labyrinthe.generate_pdf(basic=True, with_solved=True)
        elif request.form['download_content'] == 'solution':
            labyrinthe.generate_pdf(basic=False, with_solved=True)
    elif request.form['download_type'] == 'word':
        if request.form['download_content'] == 'maze':
            labyrinthe.generate_word(basic=True, with_solved=False)
        elif request.form['download_content'] == 'maze_and_solution':
            labyrinthe.generate_word(basic=True, with_solved=True)
        elif request.form['download_content'] == 'solution':
            labyrinthe.generate_word(basic=False, with_solved=True)

    return render_template('index.html', maze=labyrinthe.afficher(terminal=False), solved=False, message="Le fichier a été téléchargé avec succès.")


if __name__ == '__main__':
    app.run(debug=True,
           port=3000)