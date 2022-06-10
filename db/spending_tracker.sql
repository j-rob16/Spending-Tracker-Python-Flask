CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    wallet, INT
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

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount INT,
    product INT REFERNCES products(id) 
    user_id INT REFERENCES users(id),
    merchant_id INT REFERENCES merchants(id)
);

CREATE TABLE stocks (
    id SERIAL PRIMARY KEY,
    merchant_id INT REFERENCES merchants(id),
    product_id INT REFERENCES products(id)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255),
    product_id INT REFERENCES products(id)
)