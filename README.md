### Générateur de labyrinthes
---
Générateur de labyrinthes en ligne, codé en HTML/CSS/JS  
Le site (accessible [ici](https://labarrex.github.io/generateur-labyrinthe/)) est hébergé par GitHub Pages.

---
La structure du code est la suivante :  
- `index.html`, qui permet d'afficher le site Web, et contient (en plus de l'HTML) :
    - une balise `style` qui permet de gérer l'affichage
    - une balise `script` qui permet l'intéraction avec le site (génération des labyrinthes, export, ...)

---
Le site a été pendant un temps hébergé par DigitalOcean via Gunicorn, pour tourner avec FLask (cf. le dossier `digital_ocean`)  
Il était structuré ainsi :
- `main.py` qui permet la gestion via Flask des differentes actions,
- `labyrinthe.py` qui gère la classe Labyrinthe, et donc la génération et l'export de ceux-ci, ainsi que la création du SVG permettant l'affichage du labyrinthe,
- `templates/index.html`, qui permet l'affichage du site Web.

