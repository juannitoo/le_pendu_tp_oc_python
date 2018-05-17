# Jeu du pendu correspondant au tp openClassroom

[énnoncé de l'exercice sur openclassroom]https://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-un-bon-vieux-pendu


> Le premier point de la mission est de réaliser un jeu du pendu. Je appelle brièvement les règles, au cas où : l'ordinateur choisit un mot au hasard dans une liste, un mot de huit lettres maximum. Le joueur tente de trouver les lettres composant le mot. À chaque coup, il saisit une lettre. Si la lettre figure dans le mot, l'ordinateur affiche le mot avec les lettres déjà trouvées. Celles qui ne le sont pas encore sont remplacées par des étoiles (*). Le joueur a 8 chances. Au delà, il a perdu.
> On va compliquer un peu les règles en demandant au joueur de donner son nom, au début de la partie. Cela permettra au programme d'enregistrer son score.

J'ai modifié le nombre de chance pour 10 le comptage du score en ajoutant 1 si le mot est trouvé avant de le sauver dans le fichier

> Nous allons découper notre programme en trois fichiers :
    * Le fichier **donnees.py** qui contiendra les variables nécessaires à notre application (la liste des mots, le nombre de chances autorisées…).
    * Le fichier **fonctions.py** qui contiendra les fonctions utiles à notre application. Là, je ne vous fais aucune liste claire
    * Enfin, notre fichier **pendu.py** qui contiendra notre jeu du pendu.
