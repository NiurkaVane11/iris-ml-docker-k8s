from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib

# Cargar el dataset Iris
iris = load_iris()

# Datos de entrada (características)
X = iris.data

# Etiquetas (especies)
y = iris.target

# Crear el modelo
model = DecisionTreeClassifier()

# Entrenar el modelo
model.fit(X, y)

# Guardar el modelo entrenado
joblib.dump(model, "model.pkl")

print("Modelo entrenado y guardado como model.pkl")