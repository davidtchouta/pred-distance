# pred-distance

This is a from scratch ML flask app for my daily prediction distance based on my own distance data collected daily since three years. 
These are time series data.

# Goal : Set up an entire mlops process from data collection up to daily retraining and monitoring

## I will deploy the model locally and on cloud (Azure, AWS, GCP) using github CICD operations

This a personal project developped from scratch by me. 

## Project's steps and code

### Launch a Github Codespace 16RAM VM 

### Project structure
```plaintext
root/
├── data/
│   ├── raw_data.csv            # Données brutes
├── app/
│   ├── main.py                 # Application Flask
│   ├── model.pkl               # Modèle sauvegardé
├── scripts/
│   ├── preprocess.py           # Pré-traitement des données
│   ├── train.py                # Script pour entraîner le modèle
│   ├── predict.py              # Script pour faire des prédictions
├── tests/
│   ├── test_flask.py           # Tests unitaires pour l'API Flask
│   ├── test_model.py           # Tests pour le modèle ML
├── .github/
│   └── workflows/
│       └── ci-cd.yml           # Workflow GitHub Actions
├── requirements.txt            # Dépendances Python
├── Dockerfile                  # Fichier Docker (optionnel)
├── README.md                   # Documentation du projet
```

### Clone a repository if you want to work locally
Here we use Github Codespaces to execute code
```bash
git clone https://github.com/davidtchouta/pred-distance.git
cd pred-distance
```
### Configure a Python virtual environment 
```bash
python -m venv distenv
source distenv/bin/activate  # Sur Windows : venv\Scripts\activate
pip install --upgrade pip
```

```bash
mkdir -p app data scripts tests .github/workflows
touch app/main.py app/__init__.py scripts/preprocess.py scripts/train.py tests/test_flask.py tests/test_model.py scripts/predict.py requirements.txt Dockerfile .github/workflows/ci-cd.yml
```

