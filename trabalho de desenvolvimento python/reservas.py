import tkinter as tk
import sqlite3

def consultar_reservas():
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT reservas.id, alunos.nome, reservas.hora_reserva, reservas.duracao 
    FROM reservas
    JOIN alunos ON reservas.aluno_id = alunos.id
    ''')
    
    reservas = cursor.fetchall()
    conn.close()
    
    listbox.delete(0, tk.END)
    
    if reservas:
        for reserva in reservas:
            listbox.insert(tk.END, f"ID: {reserva[0]}, Aluno: {reserva[1]}, Hora: {reserva[2]}, Duração: {reserva[3]} horas")
    else:
        listbox.insert(tk.END, "Nenhuma reserva encontrada.")

root = tk.Tk()
root.title("Consulta de Reservas")

label = tk.Label(root, text="Reservas feitas:")
label.pack()

listbox = tk.Listbox(root, width=80, height=10)
listbox.pack()

botao_consultar = tk.Button(root, text="Consultar Reservas", command=consultar_reservas)
botao_consultar.pack()

root.mainloop()
