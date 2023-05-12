-- Create customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

-- Create orders table
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    product VARCHAR(255),
    quantity INTEGER
);

-- Insert sample data into customers table
INSERT INTO customers (name, email) VALUES
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com'),
    ('Smith', 'smith@example.com'),
    ('Lucy', 'lucy@example.com'),
    ('Elle', 'Elle@example.com');

-- Insert sample data into orders table
INSERT INTO orders (customer_id, product, quantity) VALUES
    (1, 'Tape', 5),
    (1, 'Pencil', 10),
    (2, 'Book', 3),
    (4, 'Pencil', 10),
    (1, 'Toy', 2),
    (2, 'Pencil', 20),
    (4, 'Book', 4),
    (3, 'Tape', 6),
    (5, 'Tissue', 25);
