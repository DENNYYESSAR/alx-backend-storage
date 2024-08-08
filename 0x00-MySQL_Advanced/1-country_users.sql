-- Task: Create a table named 'users' with specified attributes
-- This script creates a table 'users' with columns: id, email, name, and country.
-- The 'id' is an integer, never null, auto-incremented, and a primary key.
-- The 'email' is a string (255 characters), never null, and unique.
-- The 'name' is a string (255 characters).
-- The 'country' is an enumeration of 'US', 'CO', and 'TN', never null, with a default value of 'US'.
-- The script ensures it does not fail if the table already exists.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);
