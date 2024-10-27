CREATE DATABASE IF NOT EXISTS supermarket;

USE supermarket;

-- Table: suppliers
CREATE TABLE supplier (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100),
    contact_name VARCHAR(50),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(50),
    address VARCHAR(200),
    city VARCHAR(50),
    country VARCHAR(50)
);

-- Table: products
CREATE TABLE product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    category_name VARCHAR(50)
);

-- Table: customers
CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(50),
    address VARCHAR(200),
    city VARCHAR(100),
    country VARCHAR(100),
    registration_date DATE
);

-- Table: employees
CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    position VARCHAR(100), -- Changed from VARCHAR(5100) to a more reasonable length
    branch_id INT,
    salary DECIMAL(10, 2),
    hire_date DATE,
    termination_date DATE,
    email VARCHAR(100),
    phone VARCHAR(50),
    is_active INT
);

-- Table: branch
CREATE TABLE branch (
    branch_id INT AUTO_INCREMENT PRIMARY KEY,
    branch_type VARCHAR(50),
    city VARCHAR(50),
    country VARCHAR(100),
    phone_number VARCHAR(50),
    shop_open_date DATE
);

-- Table: payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_method VARCHAR(20),
    transaction_id VARCHAR(100),
    billing_address VARCHAR(200),
    billing_city VARCHAR(100),
    billing_country VARCHAR(100),
    payment_note VARCHAR(255)
);

-- Table: customer_orders
CREATE TABLE customer_order (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    payment_id INT UNIQUE,
    employee_id INT,
    branch_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (payment_id) REFERENCES payments(payment_id),
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
    FOREIGN KEY (branch_id) REFERENCES branch(branch_id) -- Added foreign key for branch
);

-- Table: product_orders
CREATE TABLE product_order (
    supplier_purchase_order_id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
    employee_id INT,
    branch_id INT,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
    FOREIGN KEY (branch_id) REFERENCES branch(branch_id)
);

-- Table: products_in_supplier_orders
CREATE TABLE products_in_supplier_order (
    supplier_purchase_order_id INT,
    supplier_id INT,
    product_id INT,
    order_date DATE,
    arrival_date DATE,
    quantity INT,
    unit_price DECIMAL(10, 2),
    PRIMARY KEY (supplier_purchase_order_id, product_id),
    FOREIGN KEY (supplier_purchase_order_id) REFERENCES product_order(supplier_purchase_order_id),
    FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

-- Table: products_in_customers_orders
CREATE TABLE products_in_customer_order (
    order_id INT,
    product_id INT,
    order_date DATE,
    amount DECIMAL(15, 2),
    quantities INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES customer_order(order_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

-- Table: inventory
CREATE TABLE inventory (
    product_id INT,
    branch_id INT,
    quantity INT,
    last_updated DATE,
    PRIMARY KEY (product_id, branch_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (branch_id) REFERENCES branch(branch_id)
); 