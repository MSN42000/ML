# Machine Learning Workshops

Collection of Jupyter notebooks for learning data analysis and machine learning with Python.

## Documentation
The following PDF documents provide additional information and exercises for each atelier:
- [Atelier 0](./docs/Atelier%200%20_%20Configuration%20de%20l%27environnement%20de%20travail%20pour%20le%20Machine%20Learning.pdf): Configuration de l'environnement de travail pour le Machine Learning
- [Atelier 1](./docs/Atelier%201%20_%20Introduction%20au%20Machine%20Learning%20avec%20Python.pdf): Introduction au Machine Learning avec Python
- [Atelier 2](./docs/Atelier%202%20_%20Manipulation%20des%20données%20avec%20Pandas.pdf): Manipulation des données avec Pandas
- [Atelier 3](./docs/Atelier%203%20_%20Préparation%20des%20données%20pour%20le%20Machine%20Learning.pdf): Préparation des données pour le Machine Learning

## Notebooks

- **atelier0.ipynb**: Environment setup and library verification
  - Virtual environment setup
  - Basic package installation
  - Initial testing with Iris dataset

- **atelier1.ipynb**: Python basics and first ML steps
  - Basic Python exercises
  - Data manipulation
  - Introduction to ML concepts

- **atelier2.ipynb** & **atelier2.1.ipynb**: Pandas tutorials
  - DataFrame operations
  - Data analysis
  - Visualization exercises
  - Sales data analysis

- **atelier3.ipynb**: Scikit-learn and Matplotlib
  - Iris dataset analysis
  - Random Forest classification
  - California Housing prediction
  - Model evaluation

## Setup

1. Create virtual environment: 
```bash
python -m venv ENV
```


2. Activate virtual environment:
- Windows:
```bash
.\ENV\Scripts\activate
```
- MacOS/Linux:
```bash
source ENV/bin/activate
```


3. Install dependencies:
```bash
pip install -r requirements.txt
```


4. Launch Jupyter:
```bash
jupyter notebook
```
