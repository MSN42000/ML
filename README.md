# Machine Learning Workshops

Collection of Jupyter notebooks for learning data analysis and machine learning with Python.

## Repository Structure
ml-workshops/
│
├── notebooks/
│ ├── atelier0.ipynb # Environment setup and library testing
│ ├── atelier1.ipynb # Python basics and ML introduction
│ ├── atelier2.ipynb # Pandas fundamentals
│ ├── atelier2.1.ipynb # Advanced Pandas operations
│ └── atelier3.ipynb # Scikit-learn and Matplotlib
│
├── data/
│ └── donnees_ventes.csv # Sample sales dataset
│
├── scripts/
│ ├── test_env.py # Environment test script (Iris visualization)
│ └── test_env2.py # ML model test script (Iris classification)
│
├── requirements.txt # Project dependencies
├── .gitignore # Git ignore rules
└── README.md # Project documentation
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
