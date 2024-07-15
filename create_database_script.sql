-- Create database
CREATE DATABASE IF NOT EXISTS keyword_search_volume_db;

USE keyword_search_volume_db;

-- Table for storing keywords
CREATE TABLE keyword (
    keyword_id BIGINT AUTO_INCREMENT,
    keyword_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (keyword_id)
);

-- Table for storing search volume data
CREATE TABLE keyword_search_volume (
    keyword_id BIGINT,
    created_datetime DATETIME,
    search_volume BIGINT,
    PRIMARY KEY (keyword_id, created_datetime),
    FOREIGN KEY (keyword_id) REFERENCES keyword(keyword_id)
);

-- Table for storing user subscriptions
CREATE TABLE user_subscription (
    user_id BIGINT,
    keyword_id BIGINT,
    subscription_type ENUM('hourly', 'daily') NOT NULL,
    start_time DATETIME,
    end_time DATETIME,
    PRIMARY KEY (user_id, keyword_id, subscription_type),
    FOREIGN KEY (keyword_id) REFERENCES keyword(keyword_id)
);
