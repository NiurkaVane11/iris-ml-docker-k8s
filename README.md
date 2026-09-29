# Iris ML API · FastAPI + Docker

API REST que sirve un modelo de machine learning entrenado con el dataset **Iris**: recibe las medidas de una flor y devuelve la especie predicha. El proyecto practica el flujo completo de **entrenar → serializar → servir → contenerizar** un modelo.

## Stack

- **Modelo:** scikit-learn (`DecisionTreeClassifier`)
- **API:** FastAPI + Uvicorn
- **Serialización:** joblib
- **Contenedor:** Docker (`python:3.12-slim`)

## Cómo funciona

1. `train.py` entrena un árbol de decisión con el dataset Iris y lo guarda como `model.pkl`.
2. `app.py` carga el modelo al iniciar y lo expone en una API.
3. El `Dockerfile` empaqueta la API y el modelo en una imagen lista para desplegar.

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/` | Estado de la API |
| `POST` | `/predict` | Predice la especie a partir de 4 medidas |

**Ejemplo:** las medidas son `[largo sépalo, ancho sépalo, largo pétalo, ancho pétalo]` en cm.

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d "[5.1, 3.5, 1.4, 0.2]"
```

```json
{ "class": 0 }
```

Clases: `0` = setosa, `1` = versicolor, `2` = virginica.

## Correr localmente

```bash
pip install -r requirements.txt
python train.py                 # genera model.pkl
uvicorn app:app --reload        # http://localhost:8000/docs
```

## Con Docker

```bash
docker build -t iris-api .
docker run -p 8000:8000 iris-api
```

Documentación interactiva en http://localhost:8000/docs.

## Próximos pasos

- [ ] Manifiesto de Kubernetes (`k8s.yaml`): Deployment + Service
- [ ] Pruebas automatizadas del endpoint (`test.py` con pytest)
- [ ] Validar la entrada con un modelo Pydantic y devolver el nombre de la especie
