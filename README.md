# ETUDE DE CAS - VALEURS FONCIERES

Ce code contient une analyse préliminaire sur les données de mutation, dont le but est de prédire
la valeur foncière d'un immeuble (maison ou appartement), à partir de données comme sa localisation
et les données démographiques rélatives à son code postal.

Il contient aussi une application avec une interface, où c'est possible de renseigner ces informations
sur un immeuble et reçevoir une estimation de prix de vente.


# COMMENT UTILISER CE PROJET

Le notebook Jupyter contient déjà toutes les informations nécessaires, il n'y a donc pas besoin de l'exécuter.

Pour lancer l'application, il faut d'abourd installer les librairies nécessaires avec la commande `$ pip install -r requirements.txt`.
Ensuite, dans le dossier "app" il faut lancer l'application avec la commande `python app.py`. Elle sera donc accessible à partir de l'URL http://localhost:5000/. 

L'application sert à estimer la valeur d'un bien immobilier (appartement ou maison). Une fois lancée, pour l'ustiliser, il faut
renseigner les informations suivantes:
- Code postal
- Type de local (Appartement / Maison)
- Surface réelle du bâtiment (en m2)
- Surface du terrain (en m2)
- Nombre de pièces principales
- Prix cible (le prix estimé par l'agent immobilier)


# STRUCTURE DES FICHIERS
```
case_study
│   README.md
│   exploration.ipynb
│
└───app
│   │   app.py
│   │   estimation.py
│   │   insee_code_postal
│   │   model.sav
│   │
│   └───templates
│       │   index.html
│       │   file112.txt
│   
└───data
    │   agence.csv
    │   france.csv
    │   insee_commune.csv
    │   localisation_commune.csv
```