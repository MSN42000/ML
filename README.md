# Machine Learning Workshops

Collection of Jupyter notebooks for learning data analysis and machine learning with Python.

## Repository Structure

ml/

│

├── notebooks/

│   ├── atelier0.ipynb

│   ├── atelier1.ipynb

│   ├── atelier2.ipynb

│   ├── atelier2.1.ipynb

│   └── atelier3.ipynb

│

├── scripts/

│   ├── test_env.py

│   └── test_env2.py

│

├── requirements.txt

├── .gitignore

└── README.md


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
