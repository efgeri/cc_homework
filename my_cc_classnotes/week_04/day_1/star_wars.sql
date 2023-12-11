DROP TABLE IF EXISTS lightsabers;
DROP TABLE IF EXISTS characters;

CREATE TABLE characters(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    darkside BOOLEAN,
    age INT
);

CREATE TABLE lightsabers(
    id SERIAL PRIMARY KEY,
    colour VARCHAR(255),
    hilt_metal VARCHAR(255),
    character_id INT REFERENCES characters(id) ON DELETE CASCADE
    -- on delete cascade is a constraint and it's telling SQL to delete all associated item if we delete the main entry. So if i delete my character here, it will delete the associated items.
);

INSERT INTO characters (name, darkside, age)
VALUES ('Obi-Wan Kenobi', false, 109);

INSERT INTO characters (name, darkside, age)
VALUES ('Anakin Skywalker', false, 21);

INSERT INTO characters (name, darkside, age)
VALUES ('Darth Maul', true, 99);

INSERT INTO characters (name, darkside)
VALUES ('Yoda', false);

INSERT INTO lightsabers (colour, hilt_metal, character_id)
VALUES ('green', 'gold', 4);

-- INSERT INTO lightsabers (name, darkside)
-- VALUES ('Yoda', false);

-- INSERT INTO lightsabers (name, darkside)
-- VALUES ('Yoda', false);

-- INSERT INTO lightsabers (name, darkside)
-- VALUES ('Yoda', false);