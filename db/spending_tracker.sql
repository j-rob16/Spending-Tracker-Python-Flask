DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS totals;
DROP TABLE IF EXISTS stocks;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    wallet INT
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE totals (
    id SERIAL PRIMARY KEY,
    total_spent INT,
    user_id INT REFERENCES users(id),
    merchant_id INT REFERENCES merchants(id)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price VARCHAR(255)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id), 
    user_id INT REFERENCES users(id),
    merchant_id INT REFERENCES merchants(id),
    price INT,
    date DATE,
    tag_id INT REFERENCES tags(id)
);