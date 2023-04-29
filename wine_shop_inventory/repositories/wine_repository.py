from db.run_sql import run_sql
from models.wine import Wine
from models.producer import Producer
from models.wine import Wine


def save(wine):
    sql = "INSERT INTO wines (name, description, stock_quantity, buying_cost, selling_price, producer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = (wine.name, wine.description, wine.stock_quantity, wine.buying_cost, wine.selling_price, wine.producer_id)
    results = run_sql(sql,values)
    id = results [0]['id']
    wine.id = id
    return wine
