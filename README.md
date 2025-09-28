### Générateur de labyrinthes
---
Générateur de labyrinthes en ligne, codé en Python avec Flask
Le site (accessible [ici](https://generateur-labyrinthe-kxybu.ondigitalocean.app/)) est hébergé par DigitalOcean à l'aide de Gunicorn.

---
Les differents fichiers sont :
- ```main.py``` qui permet la gestion via Flask des differentes actions,
- ```labyrinthe.py``` qui gère la classe Labyrinthe, et donc la génération et l'export de ceux-ci, ainsi que la création du SVG permettant l'affichage du labyrinthe,
- ```templates/index.html```, qui permet l'affichage du site Web.
