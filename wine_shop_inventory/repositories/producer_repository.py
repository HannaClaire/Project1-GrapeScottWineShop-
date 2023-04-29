from db.run_sql import run_sql
from models.producer import Producer
from models.wine import Wine
from models.producer import Producer

def save(producer):
    sql = "INSERT INTO producers (name) VALUES (%s) RETURNING *"
    values = (producer.name,)
    results = run_sql(sql, values)
    id = results[0]['id']
    producer.id = id
    return producer