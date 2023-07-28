CREATE TABLE IF NOT EXISTS microflora(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    count INTEGER NOT NULL,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    illumination REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);