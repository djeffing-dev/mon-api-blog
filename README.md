# mon-api-blog

**mon-api-blog** est une API simple pour la gestion des utilisateurs, articles et tags dans un blog. Ce projet a été développé dans le cadre d’un tutoriel éducatif YouTube pour démontrer les concepts suivants :

- Création d'une API avec Flask
- Connexion d'une application Flask à une base de données PostgreSQL
- Structuration d’un projet Flask
- Utilisation des routes dans un projet Flask
- Initialisation d’une base de données au démarrage d’une application Flask
- Test d’une API avec Postman et l’extension "Rest Client" de VS Code

---

## ✨ Fonctionnalités principales

- **Gestion des utilisateurs** : CRUD
- **Gestion des articles** : CRUD + ajout de tags à un article
- **Gestion des tags** : CRUD

---

## 🛠️ Technologies utilisées

### Backend
- Python
- Flask (3.1.1)

### Base de données
- PostgreSQL

### Bibliothèques importantes
- Flask
- Flask-SQLAlchemy
- python-dotenv
- psycopg2-binary

---

## 🚀 Installation et démarrage

### 1. Cloner le dépôt
```bash
git clone https://github.com/djeffing-dev/mon-api-blog.git
```

### 2. Se déplacer dans le projet
```bash
cd mon-api-blog
```

### 3. Configurer la base de données
Créez un fichier `.env` et ajoutez-y la ligne suivante en remplaçant par vos propres informations de base de données :
```
DATABASE_URL=postgresql://votre_utilisateur:votre_mot_de_passe@localhost:5432/votre_base_de_donnees
```

### 4. Créer un environnement virtuel
```bash
python -m venv venv
```

### 5. Activer l’environnement virtuel
- macOS / Linux :
    ```bash
    source venv/bin/activate
    ```
- Windows :
    ```bash
    venv\Scripts\activate
    ```

### 6. Installer les dépendances du projet
```bash
pip install -r requirements.txt
```

### 7. Lancer le projet
```bash
flask run
```

---

## 🧪 Tests
Pour utiliser l’API, vous pouvez consulter le répertoire `http-test`, où se trouvent les tests des endpoints.

---

## 📂 Structure du projet
- **Backend** : Flask
- **Base de données** : PostgreSQL
- **Tests** : Postman et "Rest Client" (extension VS Code)

---

## 📎 Liens utiles
- [Dépôt GitHub](https://github.com/djeffing-dev/mon-api-blog)

---

## 📝 Remarques
Ce projet est conçu à des fins éducatives pour apprendre à développer une API avec Flask et PostgreSQL.
