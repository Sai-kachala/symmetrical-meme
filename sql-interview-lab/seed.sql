-- Synthetic seed data. Run after schema.sql.
INSERT INTO departments (department_name) VALUES
('Engineering'), ('HR'), ('Finance'), ('Sales'), ('Operations');

INSERT INTO employees (employee_name, department_id, manager_id, salary, hire_date, email) VALUES
('Asha Rao', 1, NULL, 120000, '2021-04-12', 'asha@example.com'),
('Ravi Kumar', 1, 1, 85000, '2022-06-01', 'ravi@example.com'),
('Neha Sharma', 2, NULL, 72000, '2020-02-17', 'neha@example.com'),
('Kiran Reddy', 2, 3, 61000, '2023-01-09', 'kiran@example.com'),
('Maya Das', 3, NULL, 90000, '2019-11-05', 'maya@example.com'),
('Arjun Patel', 4, NULL, 78000, '2022-03-21', 'arjun@example.com'),
('Zoya Khan', 4, 6, 58000, '2024-07-15', 'zoya@example.com'),
('Dev Singh', 5, NULL, 65000, '2021-09-30', 'dev@example.com'),
('Isha Nair', 1, 1, 85000, '2023-05-08', 'isha@example.com'),
('Noah Joseph', NULL, NULL, 50000, '2024-02-01', 'noah@example.com');

INSERT INTO customers (customer_name, city, email, joined_on) VALUES
('Ananya', 'Vijayawada', 'ananya@example.com', '2022-01-10'),
('Bharat', 'Hyderabad', 'bharat@example.com', '2022-03-12'),
('Charan', 'Visakhapatnam', 'charan@example.com', '2023-07-20'),
('Divya', 'Hyderabad', 'divya@example.com', '2024-04-02'),
('Farah', 'Guntur', 'farah@example.com', '2024-06-15'),
('Gopal', 'Vijayawada', 'gopal@example.com', '2025-01-08'),
('Hari', 'Kakinada', 'hari@example.com', '2025-02-01');

INSERT INTO products (product_name, category, unit_price, stock_quantity) VALUES
('Keyboard', 'Electronics', 1499.00, 40),
('Mouse', 'Electronics', 699.00, 75),
('Monitor', 'Electronics', 11999.00, 15),
('Notebook', 'Stationery', 80.00, 200),
('Pen Pack', 'Stationery', 120.00, 100),
('Desk Chair', 'Furniture', 5499.00, 10),
('USB Hub', 'Electronics', 899.00, 0);

INSERT INTO orders (customer_id, order_date, status) VALUES
(1, '2025-01-04', 'paid'),
(1, '2025-02-15', 'shipped'),
(2, '2025-02-20', 'pending'),
(3, '2025-03-12', 'cancelled'),
(4, '2025-04-01', 'paid'),
(2, '2025-04-22', 'shipped'),
(5, '2025-05-10', 'paid'),
(6, '2025-05-15', 'pending');

INSERT INTO order_items (order_id, product_id, quantity, unit_price_at_purchase) VALUES
(1, 1, 1, 1499.00), (1, 2, 2, 699.00),
(2, 3, 1, 11999.00), (2, 4, 5, 80.00),
(3, 6, 1, 5499.00),
(4, 5, 2, 120.00),
(5, 3, 1, 11999.00), (5, 2, 1, 699.00),
(6, 1, 2, 1499.00), (6, 7, 1, 899.00),
(7, 4, 10, 80.00), (7, 5, 3, 120.00),
(8, 6, 1, 5499.00);
