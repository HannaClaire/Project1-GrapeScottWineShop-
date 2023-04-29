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

def select_all():
    producers = []
    
    sql = "SELECT * FROM PRODUCERS"
    results = run_sql(sql)

    for row in results:
        producer = Producer(row ['name'], row ['id'])
        producers.append(producer)
    return producers

def select(id):
    producer = None
    sql = "SELECT * FROM producers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results [0]
        producer = Producer(result['name'], result['id'])
    return producer


def delete_all():
    sql = "DELETE  FROM producers"
    run_sql(sql)
