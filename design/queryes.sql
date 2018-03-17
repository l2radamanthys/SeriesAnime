CREATE TABLE SeriesRelacion (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    relation VARCHAR (1) NOT NULL,
    serie_a_id INTEGER NOT NULL REFERENCES Series (id),
    serie_b_id INTEGER NOT NULL REFERENCES Series (id) 
);