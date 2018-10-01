DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska 
(
    id_ucznia INTEGER PRIMARY KEY,
    Nazwisko TEXT(30),
    Imie1 TEXT(20),
    Imie2 TEXT
    
);
DROP TABLE IF EXISTS dane_osobowe;
CREATE TABLE dane_osobowe
(
	Dzien NOT NULL,
	Miesiac NOT NULL,
	Rok INTEGER PRIMARY KEY,
    M_urodzenia TEXT,
    Wojewodztwo TEXT,
    id_ucznia INTEGER,
	FOREIGN KEY (id_ucznia) REFERENCES nazwiska(id_ucznia)
);
DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
	Zachowanie VARCHAR(20),
	Religia_etyka INTEGER,
	Jezyk_polski INTEGER,
    Jezyk_angielski INTEGER,
    Jezyk_niemiecki INTEGER,
    Matematyka INTEGER,
    Historia INTEGER,
    Geografia INTEGER,
    Biologia INTEGER,
    Fizyka INTEGER,
    Chemia INTEGER,
    Technika INTEGER,
    Informatyka INTEGER,
    Plastyka INTEGER,
    PO INTEGER,
    W-F INTEGER,
    id_ucznia INTEGER,
	FOREIGN KEY (id_ucznia) REFERENCES nazwiska(id_ucznia)
);
