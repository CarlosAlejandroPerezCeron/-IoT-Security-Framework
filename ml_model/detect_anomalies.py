import pandas as pd
import joblib

# Cargar modelo de Machine Learning
model = joblib.load("ml_model/model.pkl")

# Leer datos de tráfico IoT
data = pd.read_csv("data/traffic_logs.csv")

# Realizar predicción
predictions = model.predict(data)

# Guardar anomalías detectadas
anomalies = data[predictions == 1]
anomalies.to_csv("data/anomalies.csv", index=False)

print("✅ Análisis completado. Anomalías guardadas en data/anomalies.csv")
