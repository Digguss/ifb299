CREATE SCHEMA 'new_database' ;

CREATE TABLE 'new_database'.'sites_tourist' {
	'ID' INT NOT NULL AUTO_INCREMENT,
	'Name' VARCHAR(45) NULL,
	'Location' VARCHAR(45) NULL,
	'Type' VARCHAR(45) NULL,
	'Link' VARCHAR(45) NULL,
	'Picture' VARCHAR(45) NULL,
	PRIMARY KEY ('ID'));
}