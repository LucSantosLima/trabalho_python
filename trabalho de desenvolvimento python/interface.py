import tkinter as tk
from tkinter import messagebox
import sqlite3

def verificar_matricula():
    matricula = entrada_matricula.get()
    
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos WHERE matricula = ?', (matricula,))
    aluno = cursor.fetchone()
    conn.close()

    if aluno:
        fazer_reserva(aluno[0])  
    else:
        messagebox.showerror("Erro", "Aluno não matriculado!")

def fazer_reserva(aluno_id):
    hora_reserva = entrada_hora.get()
    duracao_reserva = entrada_duracao.get()
    
    if not hora_reserva or not duracao_reserva:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return
    
    try:
        duracao_reserva = int(duracao_reserva)
        if duracao_reserva < 1 or duracao_reserva > 4:
            messagebox.showerror("Erro", "Duração inválida! (1 a 4 horas)")
            return
    except ValueError:
        messagebox.showerror("Erro", "A duração deve ser um número entre 1 e 4!")
        return

    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO reservas (aluno_id, hora_reserva, duracao) 
    VALUES (?, ?, ?)
    ''', (aluno_id, hora_reserva, duracao_reserva))
    
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", "Reserva realizada com sucesso!")

def cadastrar_aluno():
    nome = entrada_nome.get()
    matricula = entrada_matricula_cadastro.get()

    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO alunos (nome, matricula) 
    VALUES (?, ?)
    ''', (nome, matricula))
    
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")

app = tk.Tk()
app.title("Reserva de Quartos")

tk.Label(app, text="Matrícula:").pack()
entrada_matricula = tk.Entry(app)
entrada_matricula.pack()

tk.Label(app, text="Hora da Reserva (HH:MM):").pack()
entrada_hora = tk.Entry(app)
entrada_hora.pack()

tk.Label(app, text="Duração (1-4 horas):").pack()
entrada_duracao = tk.Entry(app)
entrada_duracao.pack()

tk.Button(app, text="Verificar Matrícula", command=verificar_matricula).pack()

tk.Label(app, text="Nome do Aluno (Cadastro):").pack()
entrada_nome = tk.Entry(app)
entrada_nome.pack()

tk.Label(app, text="Matrícula (Cadastro):").pack()
entrada_matricula_cadastro = tk.Entry(app)
entrada_matricula_cadastro.pack()

tk.Button(app, text="Cadastrar Aluno", command=cadastrar_aluno).pack()

app.mainloop()
