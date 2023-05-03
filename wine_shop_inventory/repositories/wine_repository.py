from db.run_sql import run_sql
from models.wine import Wine
from models.producer import Producer
from models.wine import Wine
import repositories.producer_repository as producer_repo
import repositories.wine_repository as wine_repo



def save(wine):
    sql = "INSERT INTO wines (name, description, stock_quantity, buying_cost, selling_price, producer) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = (wine.name, wine.description, wine.stock_quantity, wine.buying_cost, wine.selling_price, wine.producer)
    results = run_sql(sql,values)
    id = results [0]['id']
    wine.id = id
    return wine


def select_all():
    wines = []

    sql = "SELECT * FROM wines"
    results = run_sql(sql)

    for row in results:
        producer = producer_repo.select(row['producer'])
        wine = Wine (row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], producer, row['id'])
        wines.append(wine)
    return wines


def delete_all():
    sql = "DELETE  FROM wines"
    run_sql(sql)



def select(id):
    wine = []
    sql = "SELECT * FROM wines WHERE id = %s"
    values = [id,]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        producer = producer_repo.select(result['producer'])
        wine = Wine(result ['name'], result['description'], result['stock_quantity'], result['buying_cost'], result['selling_price'], producer, result['id'])
        return wine
    


def update_wine(wine):
    sql = "UPDATE wines SET (name, description, stock_quantity, buying_cost, selling_price, producer) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [wine.name, wine.description, wine.stock_quantity, wine.buying_cost, wine.selling_price, wine.producer.id, wine.id]
    run_sql(sql, values)


#technically extension?
def get_wines_for_producer(producer):
    #  get all the wines
    wines = []
    sql = "SELECT * FROM wines WHERE producer = %s"
    values = [producer]
    results = run_sql(sql, values)

    for row in results:
        wine = Wine(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], producer, row['id'])
        wines.append(wine)
    return wines
    
    
    
    
    # if results:
    #     result = results[0]
    #     producer = producer_repo.select(result['producer_id'])
    #     wines = Wine(result['name'], result['description'], result['stock_quantity'],
    #                 result['buying_cost'], result['selling_price'], producer, result['id'])
    #     return wines

