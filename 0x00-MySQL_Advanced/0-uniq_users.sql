-- ensuring comment on all lines
-- to be ddited later

CREATE TABLE IF NOT EXIST users (
	id INTEGER NOT NULL AUTO INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	);
