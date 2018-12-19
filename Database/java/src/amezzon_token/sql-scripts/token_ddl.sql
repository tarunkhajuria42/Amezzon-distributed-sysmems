CREATE TABLE IF NOT EXISTS tokens
(
  token VARCHAR
(
  36
) NOT NULL PRIMARY KEY,
  username VARCHAR
(
  40
) NOT NULL
  CONSTRAINT username_uindex UNIQUE
(
  username
),
  );
