# Claude · La Boutique du Menuisier Tignieu-Jameyzieu

Landing page de demande de chiffrage pour Claude, conseiller de l'agence TPM – La Boutique du Menuisier (65 route de Crémieu, 38230 Tignieu-Jameyzieu).

## Contenu
- `index.html` : la page en ligne (un seul fichier, aucune dépendance).
- `claude.jpg` : photo de Claude, à déposer à la racine (format portrait, visage bien visible). Sans photo, un monogramme s'affiche.
- `src/page.html` + `build.py` : source de la page ; `python3 build.py` régénère `index.html`.

## Réception des demandes
Les demandes sont envoyées par e-mail via FormSubmit à l'adresse définie en haut du script (`CONFIG.endpoint`, par défaut contact@tpm38.fr).
La toute première demande déclenche un e-mail d'activation à cette adresse : il faut cliquer sur le lien une fois.

## Mise en ligne
GitHub Pages : Settings › Pages › Deploy from branch › `main` / root.
