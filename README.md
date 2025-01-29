# Analyse et Visualisation de données avec MongoDB, FastAPI et Streamlit

## Description du projet

Ce projet a pour objectif d’explorer et de comprendre les données en utilisant des outils modernes comme <span style="font-family: Arial, sans-serif;">**MongoDB**</span>, <span style="font-family: Arial, sans-serif;">**FastAPI**</span> et <span style="font-family: Arial, sans-serif;">**Streamlit**</span>. **MongoDB** sert de base de données NoSQL pour stocker et manipuler les informations, tandis que **FastAPI** est utilisé pour créer une API performante permettant d’extraire et d’analyser ces données. Enfin, **Streamlit** est utilisé pour offrir une interface visuelle simple et intuitive afin de présenter de manière claire et interactive les KPI (indicateurs clés de performance).

## Objectifs

L’objectif de ce projet est d’explorer différentes étapes clés de la gestion et de la visualisation des données :

- **Configurer MongoDB** pour stocker les données de manière flexible.
- **Importer des données CSV** et les organiser efficacement dans la base de données MongoDB.
- **Créer une API performante avec FastAPI** pour extraire et manipuler les données en temps réel.
- **Visualiser les résultats via Streamlit**, un outil interactif pour rendre les données compréhensibles et accessibles.

## Technologies utilisées

- <span style="font-family: Arial, sans-serif;">**MongoDB**</span> : Base de données NoSQL pour gérer les données non structurées et volumineuses.
- <span style="font-family: Arial, sans-serif;">**FastAPI**</span> : Framework moderne et rapide pour créer des API, permettant d'interagir avec MongoDB.
- <span style="font-family: Arial, sans-serif;">**Streamlit**</span> : Bibliothèque Python qui facilite la création d’applications web interactives pour la visualisation des données.

### Pourquoi ces technologies ?

- **MongoDB** a été choisi pour sa flexibilité et sa capacité à gérer des données non structurées. Contrairement aux bases relationnelles comme <span style="font-family: Arial, sans-serif;">**PostgreSQL**</span>, MongoDB est mieux adapté pour les données en grande quantité et pour les relations flexibles.
  
- **FastAPI** est un choix judicieux pour créer des APIs rapides et performantes, avec la génération automatique de la documentation via Swagger. Cela permet de simplifier l’interaction avec les données stockées dans MongoDB.

- **Streamlit** est utilisé pour sa simplicité d’utilisation et sa capacité à créer des dashboards interactifs en quelques lignes de code, sans avoir besoin de connaissances approfondies en développement web.

## Prérequis

Les prérequis nécessaires au bon fonctionnement du projet sont :

- **Python 3** : Langage de programmation utilisé pour ce projet.
- **MongoDB** : Base de données NoSQL pour le stockage des données.
- **Streamlit** : Outil de visualisation des données interactif.
- **FastAPI** : Framework Python pour la création d'API rapides.

## Installation

Voici les étapes pour installer et faire fonctionner ce projet :

1. **Clonez le projet depuis GitHub** :

   ```bash
   git clone https://github.com/Zaza9216/projet_backend.git

2. **Créez un environnement virtuel** :

#Sous Mac/Linux

   ```bash
python -m venv env
source env/bin/activate
```
#Sous Windows 

```bash
python -m venv env
env\Scripts\activate
```
3. **Installez les bibliothèques nécessaires : Installez toutes les bibliothèques listées dans le fichier requirements.txt pour faire fonctionner le projet** :

```bash
pip install -r requirements.txt
```
4. **Lancez le serveur MongoDB : Assurez-vous que MongoDB est installé et démarrez-le en exécutant***:

```bash
mongod
```
5. **Importez les données dans MongoDB : Importez les fichiers CSV dans MongoDB en exécutant le script Python suivant**:

```bash
python import_data.py
````
6. **Démarrez l'API FastAPI : Exécutez la commande suivante pour démarrer le backend FastAPI, qui permet d'extraire les KPI depuis la base de données**:

```bash
uvicorn main:app --reload
````

7. **Lancez l'interface Streamlit : Démarrez l'application Streamlit pour visualiser les KPI et les graphiques**:

```bash
streamlit run app.py
```
## Description des fichiers du projet

Voici une brève description des fichiers présents dans le dépôt :

- **app.py** : Ce fichier gère l'application Streamlit. Il permet d'afficher les données de manière visuelle et interactive, permettant d'explorer les KPI et de comprendre les résultats.

- **main.py** : Le cœur de l'API FastAPI. Ce fichier définit les différentes routes permettant de récupérer et manipuler les données stockées dans MongoDB. Il expose les données via des requêtes web.

- **import_data.py** : Script Python utilisé pour importer les fichiers CSV dans MongoDB. Il facilite la préparation et l'intégration des données afin qu'elles soient prêtes à être utilisées dans l'application.

- **mongodb_aggregation.py** : Ce fichier contient des requêtes d'agrégation MongoDB pour effectuer des calculs et des analyses avancées sur les données, comme la génération de statistiques et d'indicateurs clés.

- **requirements.txt** : Ce fichier contient la liste complète des bibliothèques Python nécessaires pour faire fonctionner le projet. Installez-les avec la commande suivante :

```bash
pip install -r requirements.txt
````

### Étapes d'exécution du code

- **Lancer l'API** : Exécutez la commande suivante pour démarrer le backend FastAPI :

```bash
uvicorn main:app --reload
````
- **Démarrer Streamlit** : Lancez l'application Streamlit avec la commande suivante pour la visualisation des KPI et graphiques :

```bash
streamlit run app.py
````


