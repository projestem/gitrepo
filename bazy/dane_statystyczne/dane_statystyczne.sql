DROP TABLE IF EXISTS miasta;
CREATE TABLE miasta 
(
    id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa_miasta TEXT(30),
    wojewodztwo TEXT(20)
    
);

DROP TABLE IF EXISTS mieszkancy;
CREATE TABLE mieszkancy
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	liczba_mieszkancow INTEGER,
	liczba_kobiet INTEGER,
	grupa_wiekowa TEXT(20),
    data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
);

DROP TABLE IF EXISTS powierzchnie;
CREATE TABLE powierzchnie
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	powierzchnia_miasta DECIMAL,
	powierzchnia_terenow_zielonych DECIMAL(10),
	data_aktualizacji DATE,
    id_miasta INTEGER,
	FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
);
