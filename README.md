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

### add xlsx database in data folder

### install library to read xlsx file
```python
pip install pandas openpyxl
```

### Creation and Editing a jupyter notebook preprocess.ipynb to read a xlsx file

Warning : Make sure to select your python virtual environment to run the code

###create a git branch 
```bash
//verify the active branch
git branch
//go the specific branch
git checkout develop
// update the basis branch (not mandatory but recommended)
git pull origin develop
// Create and jump in the new branch
git checkout -b data-cleaning
git checkout -b data-analysis
// push in the distant folder (recommended)
git push -u origin data-cleaning
git push -u origin data-analysis
```

### Before pull request creation :
```bash
# 1. Update develop branch
git checkout develop
git pull origin develop

# 2. go to the data-cleaning branch
git checkout data-cleaning

# 3. Merge develop in data-cleaning to avoid conflicts 
git merge develop

# 4. Push changes
git push origin data-cleaning
```

## Step 2: Create the Pull Request on GitHub
Once your branch is up to date and your changes have been pushed, you can create the pull request via the GitHub interface.

1. Go to your repository on GitHub.
2. Open the "Pull requests" tab.
3. Click on the "New pull request" button.
4. In the dropdown menus, select:
   - **Base**: `develop`
   - **Compare**: `data-cleaning`
5. Add a title and description to explain the changes made.
6. Click on "Create pull request."

## Step 3: Review and Validation
Once the pull request is created:
1. Other project members (if applicable) can review your changes.
2. Resolve any conflicts and make further modifications if necessary.
3. When everything is ready, the pull request can be merged into the `develop` branch.

## Step 4: Merge the Pull Request
If you have the necessary permissions, you can merge the pull request by clicking on "Merge pull request."
Otherwise, another collaborator will be able to merge it.
