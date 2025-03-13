# PredictHealth Front & API

PredictHealth est un tableau de bord interactif conçu pour l'hôpital Pitié-Salpêtrière. Le projet se compose de deux parties principales :

- **Front-end** : Une application Vue.js (avec Vite) qui permet de visualiser dynamiquement les indicateurs et graphiques (ex. évolution des admissions, répartition par jour de la semaine) en fonction de filtres.
- **Back-end (API)** : Une API développée avec FastAPI qui interroge un fichier CSV contenant 4 ans de données quotidiennes (76 colonnes) pour fournir des statistiques agrégées et des prédictions.

---

## 🚀 Technologies Utilisées

### Front-end
- **Vue.js 3** : Framework JavaScript pour le développement de l'interface.
- **Vite** : Outil de build rapide et léger.
- **Vue Router** : Pour la navigation entre les pages.
- **Vuetify** : UI Kit pour des composants stylés (optionnel).

### Back-end (API)
- **FastAPI** : Framework web rapide et moderne pour créer des APIs.
- **Uvicorn** : Serveur ASGI pour exécuter FastAPI.
- **Pandas** et **Numpy** : Pour la manipulation et l'analyse des données.
- **Python 3.9+**

---

## 📦 Installation et Lancement du Projet

### 1. Front-end

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/LoicChazeau/PredictHealth
   cd PredictHealth
   ```

2. **Installer les dépendances** :
    ```bash
    npm install
    ```

3. **Lancer le serveur de développement** :
    ```bash
    npm run dev
    ```
    Le projet sera accessible sur **http://localhost:5173**.

---

## Lancer l'API (Back-end)

1. Ouvrez un terminal et naviguez dans le répertoire dédié à l'API (par exemple, `cd PredictHealth-api`).

2. **(Optionnel)** Créez et activez un environnement virtuel (recommandé) :
    ```bash
    python -m venv venv
    # Sous Windows :
    venv\Scripts\activate
    # Sous macOS/Linux :
    source venv/bin/activate
    ```

3. Installez les dépendances Python avec :
    ```bash
    pip install -r requirements.txt
    ```
    *Exemple de contenu de `requirements.txt` :*
    ```
    fastapi
    uvicorn
    pandas
    numpy
    ```

4. Assurez-vous que le fichier CSV (`Global_dataset.csv`) se trouve dans le répertoire racine de l'API.

5. Lancez le serveur API avec :
    ```bash
    uvicorn server:app --reload --host 0.0.0.0 --port 8000
    ```
    L'API sera alors accessible sur **http://localhost:8000**.

---

## Utilisation et Fonctionnalités

- **Filtres dynamiques** :  
  Le front-end permet de sélectionner un service et une année (de 2020 à 2024, avec une option "Toutes les années"). Ces filtres influencent l'affichage des graphiques.

- **Graphiques dynamiques** :  
  Deux graphiques principaux s'affichent sur la page "Admissions" :
  1. **Évolution mensuelle des admissions** : Visualisation de la tendance des admissions sur l'année sélectionnée.
  2. **Répartition des admissions par jour de la semaine** : Visualisation de la charge quotidienne, regroupée par jour.

- **Endpoints clés de l'API** :
  - `GET /filters` : Renvoie les options disponibles pour les filtres (services, années, plage de dates).
  - `GET /dashboard` : Renvoie les indicateurs clés (admissions totales, taux d’occupation, temps d’attente, etc.).
  - `GET /admissions/evolution` : Renvoie l'évolution mensuelle des admissions en fonction des filtres.
  - `GET /admissions/distribution` : Renvoie la répartition des admissions par jour de la semaine selon les filtres.
  - `GET /data` et `GET /predict/{date}` : Endpoints supplémentaires pour obtenir les données brutes ou des prédictions.

---
