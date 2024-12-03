from sklearn.datasets import load_iris  # Importer la fonction pour charger le dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# Chargement du dataset Iris
iris = load_iris()
# Données et cibles
X = iris.data
y = iris.target
# Division en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Modèle
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
# Prédictions
y_pred = model.predict(X_test)
print("Précision du modèle :", accuracy_score(y_test, y_pred))
