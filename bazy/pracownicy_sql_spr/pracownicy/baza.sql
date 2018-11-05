DROP TABLE IF EXISTS pracownicy;
CREATE TABLE pracownicy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie VARCHAR(15),
    nazwisko VARCHAR(15),
    kod VARCHAR(7),
    miasto_z VARCHAR(20),
    ulica VARCHAR(20),
    data_ur DATE,
    miasto_u VARCHAR(20)
);
 
DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska (
    id_s INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko VARCHAR(15)
);
 
DROP TABLE IF EXISTS kontakty;
CREATE TABLE kontakty (
        id_pracownika INTEGER NOT NULL,
        typ_k TINYINT,
        kontakt VARCHAR(15),
        uwagi VARCHAR(15),
        FOREIGN KEY(id_pracownika) REFERENCES pracownicy(id)
);
 
DROP TABLE IF EXISTS place;
CREATE TABLE place (
        id_p INTEGER NOT NULL,
        id_s INTEGER,
        placa INTEGER,
        data_z DATE,
        FOREIGN KEY(id_p) REFERENCES pracownicy(id),
        FOREIGN KEY(id_s) REFERENCES stanowiska(id_s)
);

