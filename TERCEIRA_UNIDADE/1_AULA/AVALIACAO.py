# Vamos pensar no problema apresentado no início desta aula! O objetivo é criar a tabela “Contatos” 
# para armazenar informações de contatos, incluindo nome, e-mail e número de telefone.

import sqlite3

# Criacao da tabela e insercao de dados de exemplo
conn = sqlite3.connect('contatos.sb')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Contatos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               email TEXT,
               telefone TEXT)
""")

dados_exemplo = [
    ('Joao', 'joao@email.com', '123-456-7890')
    ('Maria', 'maria@email.com', '0987-654-321')
    ('Carlos', 'carlos@email.com', '654-321-7890')
]
cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES (?, ?, ?)', dados_exemplo)
conn.commit()

# Leitura e exibicao dos contatos
cursor.execute('SELECT * FROM Constatos')
contatos = cursor.fetchall()
print("Contatos: ")
for contato in contatos:
    print(contato)

# Atualizacao do numero de telefone do contato com ID 3
novo_telefone = '999-999-9999'
contato_id = 3
cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
conn.commit()

# Exclusao do contato com ID 2
contato_id_excluir = 2

cursor.execute('DELETE FROM Contatos WHERE id = ?', (contato_id_excluir,))
conn.commit()

# Fechando conexao
conn.close()