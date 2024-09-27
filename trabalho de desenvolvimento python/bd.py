import sqlite3

conn = sqlite3.connect('reservas.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reservas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    hora_reserva TEXT NOT NULL,
    duracao INTEGER NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
)
''')

conn.commit()
conn.close()
