# Schéma du SNDS

Le SNDS est une collection de base de données, difficile à documenter et à manipuler.

Ce schéma du SNDS **centralise** une description du SNDS sous un format **standard**.
 
 
## Utilité

Ce schéma permet de générer des documentations dans plusieurs formats, actuellement :
- un [dictionnaire interactif](http://dico-snds.health-data-hub.fr/) des variables et des liens entre tables,
- une [documentation textuelle](http://documentation-snds.health-data-hub.fr/) (section `tables`).

Il est envisagé d'utiliser ce schéma pour générer d'autres supports de documentations, et pour configurer des codes qui manipulent les données.

Un diagramme relationnel du SNDS au format pdf est par exemple généré, en créant des tables vides dans une base PostgreSQL puis en analysant son contenu avec [SchemaCrawler](http://schemacrawler.com/).

Nous projetons également d'ajouter des valeurs exemples pour chaque variable, 
afin de générer des jeux de données synthétiques respectant la structure formelle du SNDS.


## Modifier le schéma

Le schéma est formalisé en suivant la spécification Table Schema, présentée dans ce [document](documentation/Table-Schema.md).

Vos propositions de corrections et d'améliorations sont bienvenues.

Pour cela vous pouvez :
- éditer directement les fichiers json dans le dossier [schemas](schemas) et ouvrir une `merge-request`,
- ouvrir une `issue`,
- écrire à l'équipe du Lab Santé à la [DREES](https://drees.solidarites-sante.gouv.fr/etudes-et-statistiques/), qui développe et maintient ce projet : [ld-lab-github@sante.gouv.fr](mailto:ld-lab-github@sante.gouv.fr). 


## Installation du projet pour générer les produits dérivés

**Dépendances** : python3, virtualenv, Docker, Docker-Compose, git

Activation d'un environnement virtuel Python avec les dépendances installées  

    ./create_vitualenv.sh
    source venv/bin/activate

Utilisation 

    ./main.py -h


Pour des explications détaillées, se référer au fichier [INSTALL.md](INSTALL.md)


## Historique 

La première version du schéma provient d'un travail 
[archivé ici](https://gitlab.com/healthdatahub/dico-snds-creation-archive), 
basé sur des documents de la [Caisse Nationale d'Assurance Maladie](https://assurance-maladie.ameli.fr/qui-sommes-nous). 


## Mentions

Ce projet a été initié dans le cadre du programme 
[« Entrepreneurs d'intérêt général »](https://entrepreneur-interet-general.etalab.gouv.fr/), 
pour le projet [Open Chronic](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2019/openchronic.html).
