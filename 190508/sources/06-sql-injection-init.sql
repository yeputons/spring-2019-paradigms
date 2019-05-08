DROP TABLE IF EXISTS Text;
CREATE TABLE Text (owner TEXT, key TEXT, value TEXT);
INSERT INTO Text (owner, key, value)
VALUES ("user", "key1", "value1"),
       ("user", "key2", "value2"),
       ("user", "other key", "value3"),
       ("admin", "key1", "secret_value");
