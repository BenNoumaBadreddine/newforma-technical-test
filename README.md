# Test technique Newforma 

# Mise en situation
Certains promoteurs de projet tentent de comprendre comment augmenter le taux de réussite de leurs futures campagnes. Ils ont à leur disposition des données historiques de campagnes annoncées sur la plateforme Kickstarter.
# Objectif
Développe en Python une approche ML (supervisée et/ou non supervisée) pour aider les promoteurs de projet à lancer des campagnes à fort potentiel de réussite.
# Hypothèses

Toutes mes notes et mes hypothèses que j'ai fixées sont écrites dans les cellules de jupyter notebook.
Avant de commencer la résolution d'une tâche dans le processus de création de la méthode d'apprentissage machine, j'essaye de noter toute interprétation, conclusion, hypothèses, explication dans des cellules de jupyter notebook.


# Structure du projet

La structure du projet est la suivante:

* Dossier **outputs**: contient les résultats de la prédiction,
* Dossier **models**: contient les modeles de prediction,
* Dossier **results_data_profiling**: contient un fichier html contenant une analyse complète  des données,
* Dossier **data**: contient les fichiers csv des données brutes et preprocessées.
* Dossier **docs**: contient les fichiers contenant la documentation du projet ainsi que le document contenant la réponse aux questions,
* Dossier **images**: contient des images,
* Dossier **src**: contient des scripts python contenant les fonctions utilisées pour exécuter le processus de préparation, analyse des données ainsi que la création des  modèles de ML,
* Dossier **tests**: devrait contenir des scripts python avec les fonctions de test de chaque fonction utilisée dans le projet,
* Dossier **notebooks**: contient des jupyter notebook décrivant le processus d'élaboration du projet:
  - **0-loading_the_data_define_variables.ipynb**: contient le code pour importer les données et les bibliothèques 
  - **1-data_understanding.ipynb**: contient le code pour comprendre la structure des données et les différentes colonnes.
  - **2-exploratory_data_analysis_EDA.ipynb**: contient le code pour l’analyse exploratoire des donnees.
  - **3-advanced_analysis.ipynb**: contient le code pour analyser davantage les donnees et montrer les corrélations et les relations entre les variables ainsi que le poids de chacun sur la prédiction de ‘state’ du projet.
  - **4-data_preprocessing.ipynb**: contient le code à suivre pour exécuter le pipeline des données qui consiste à l'importation, transformation, extraction et création des nouveaux features.
  - **5-model_baseline.ipynb**: contient le code pour la création et l'évaluation de plusieurs algorithmes d’apprentissage machine permettant d'exécuter la tâche de prédiction du succès d’un projet avant de le lancer sur la plate-forme Kickstarter.