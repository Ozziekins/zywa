CREATE DATABASE card_status;

CREATE TABLE card_status_table (
    id SERIAL PRIMARY KEY,
    card_id VARCHAR(255) NOT NULL,
    user_mobile VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    status VARCHAR(255) NOT NULL,
    comment TEXT
);
