mon-api-blog est une API simple de gestion (utilisateurs articles, tag) dans un blog.
Ce projet a été développé dans le cadre d’un tutoriel éducatif YouTube pour démontrer comment :

Créer une API avec Flask
Connecter une application Flask à une base de données PostgreSQL
Comment structurer un projet flask
Utiliser les routes dans un projet flask
Initialiser une base de données au demarmarage d'une application flask
Tester une API avec Postman et "Rest client" une extension de Vscode

✨ Fonctionnalités principales
Gestion des utilisateurs (CRUD)
Gestion des articles (CRUD) + ajouter d'un tag a un article
Gestion des tags (CRUD)

🛠️ Technologies utilisées
Backend
Python
Flask (3.1.1)

Base de données

PostgreSQL
SQLAlchemy / JPA

Bilbliothèques importantes
 - Flask
 - Flask-SQLAlchemy
 - python-dotenv
 - psycopg2-binary

Installation et démarrage
1. Cloner le depot
   git clone https://github.com/djeffing-dev/mon-api-blog.git

2. se deplacer dans le projet
    cd mon-api-blog

3. Configurer la base de données 
   crée un fichier ".env", ajouter cette ligne dans le ficchier et la completer par vos propre information de base de donnéés
   DATABASE_URL=postgresql://votre_utilisateur:votre_mot_de_passe@localhost:5432/votre_base_de_donnees

4. crée un environement virtuel
   python -m venv venv

5. lancer votre environement virtuelle
    - macOS / Linux : source venv/bin/activate
    - Windows : venv\Scripts\activate

6. installer les dependance du projet:
   - pip install requirements.txt

7 - lancer le projet :
    -  flask run

pour utiliser l'api, vous pour consulter le repertoire http-test, ou se trouve les tests des endpoind