/* schema.sql */

DROP TABLE IF EXISTS backpacks;

CREATE TABLE IF NOT EXISTS backpacks
(
  make VARCHAR(8), model VARCHAR(25), price DECIMAL(6,2)
);

