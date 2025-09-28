from flask import *
from labyrinthe import Labyrinthe

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

    download_type = request.form['download_type']
    download_content = request.form['download_content']
    
    # Déterminer les paramètres pour la génération
    basic = download_content in ['maze', 'maze_and_solution']
    with_solved = download_content in ['maze_and_solution', 'solution']
    
    # Générer le nom de fichier
    if download_content == 'maze':
        content_suffix = ""
    elif download_content == 'maze_and_solution':
        content_suffix = " avec solution"
    else:  # solution
        content_suffix = " résolu"
    
    if download_type == 'pdf':
        # Générer le PDF en mémoire
        pdf_data = labyrinthe.generate_pdf_bytes(basic=basic, with_solved=with_solved)
        
        filename = f'labyrinthe_{labyrinthe.largeur}x{labyrinthe.hauteur}{content_suffix}.pdf'
        
        # Créer la réponse avec le fichier PDF
        response = make_response(pdf_data)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
        
    elif download_type == 'word':
        # Générer le document Word en mémoire
        word_data = labyrinthe.generate_word_bytes(basic=basic, with_solved=with_solved)
        
        filename = f'labyrinthe_{labyrinthe.largeur}x{labyrinthe.hauteur}{content_suffix}.docx'
        
        # Créer la réponse avec le fichier Word
        response = make_response(word_data)
        response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response

    # Si on arrive ici, quelque chose s'est mal passé
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)
