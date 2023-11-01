import psycopg2
from tkinter import *

conn = psycopg2.connect(
    host="localhost",
    database="banco31102023",
    user="postgres",
    password="1236"
)
curr = conn.cursor()

def criaTabela():
    curr.execute('CREATE TABLE funcionarios '
                    ' ( nome varchar(19))'
                    )
    conn.commit()

criaTabela()

def insereNomeTabela():
    nomeDigitado = entrada.get()
    sql = """INSERT INTO funcionarios (nome) VALUES (%s)"""

    print(sql, nomeDigitado)
    curr.execute(sql, (nomeDigitado,))
    conn.commit()

def DeleteNomeTabela():
    nomeDigitado = entrada.get()
    sql = """DELETE FROM funcionarios where nome = %s"""

    print(sql, nomeDigitado)
    curr.execute(sql, (nomeDigitado,))
    conn.commit()

def UpdateNomeTabela():
    nomeDigitado = entrada.get()
    UpdateNome = entradaUpdate.get()
    sql = """UPDATE funcionarios set nome = %s where nome = %s"""

    print(sql, nomeDigitado)
    curr.execute(sql, (nomeDigitado, UpdateNome,))
    conn.commit()

def SelecionaNomeTabela():
    curr.execute('SELECT * FROM FUNCIONARIOS')
    registros = curr.fetchall()

    dados = "\n".join([f"Nome: {registro[0]}" for registro in registros])
    label_dados["text"] = dados 

root = Tk()

texto = Label(root, text='Digite seu nome')
texto.pack(pady= 5)

entrada = Entry(root)
entrada.pack(pady= 5)


botao = Button(root, text='Enviar nome', command=insereNomeTabela)
botao.pack(pady= 5)


botaoDelete = Button(root, text='Deletar nome', command=DeleteNomeTabela)
botaoDelete.pack(pady= 5)

entradaUpdate = Entry(root)
entradaUpdate.pack(pady= 5)

texto = Label(root, text='Digite o nome que deseja renomear')
texto.pack(pady= 5)


botaoUpdate = Button(root, text='Renomear nome', command=UpdateNomeTabela)
botaoUpdate.pack(pady= 5)


label_dados = Label(root, text="", wraplength=300)
label_dados.pack(pady=5)

tudoBanco = Button(root, text='Selecionar todos', command=SelecionaNomeTabela)
tudoBanco.pack(pady=5)


root.geometry("300x400")
root.mainloop()

