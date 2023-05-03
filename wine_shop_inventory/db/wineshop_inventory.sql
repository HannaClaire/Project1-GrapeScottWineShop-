DROP TABLE IF EXISTS wines;
DROP TABLE IF EXISTS producers;

CREATE TABLE producers (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
);


CREATE TABLE wines (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    description TEXT,
    stock_quantity INT,
    buying_cost INT,
    selling_price INT,
    producer INT NOT NULL REFERENCES producers(id)
);
