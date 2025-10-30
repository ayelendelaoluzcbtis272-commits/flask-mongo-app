from pymongo import MongoClient
import os

MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://luzayelen:admin123@cluster0.9peejhd.mongodb.net/escuela")
client = MongoClient(MONGO_URI)
db = client.get_default_database()

db.alumnos.delete_many({})

alumnos = [
    {"nombre": "Ana López", "edad": 16, "grupo": "3A", "promedio": 8.7},
    {"nombre": "Juan Pérez", "edad": 17, "grupo": "3B", "promedio": 7.9},
    {"nombre": "María García", "edad": 15, "grupo": "2A", "promedio": 9.2},
]

db.alumnos.insert_many(alumnos)
print("Seed completado. Registros insertados:", db.alumnos.count_documents({}))
