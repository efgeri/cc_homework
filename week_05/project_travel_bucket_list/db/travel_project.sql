DROP TABLE users_cities;
DROP TABLE users;
DROP TABLE sights;
DROP TABLE cities;
DROP TABLE countries;
DROP TABLE continents;

CREATE TABLE continents (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  continent_id INT NOT NULL REFERENCES continents(id) ON DELETE CASCADE
);

CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  visited BOOLEAN,
  visit_date DATE,
  country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE sights (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  visit_date VARCHAR(255),
  visited BOOLEAN,
  city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255),
  name VARCHAR(255)
);


CREATE TABLE users_cities (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE
);