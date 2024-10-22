import sqlite3

# Conectar ao banco de dados SQLite (Caso nao exista, criar)
conn = sqlite3.connect("funcionarios2.db")

# Criar a tabela de funcionarios
cursor = conn.cursor()
cursor = conn.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS funcionarios2 (

        id INTEGER PRIMARY KEY,

        nome TEXT,

        cargo TEXT,

        salario REAL

    )

''')

# Inserir um novo funcionario na tabela
novo_funcionario = (1, "João", "Analista", 5000.00)
cursor.execute("INSERT INTO funcionarios2 VALUES (?, ?, ?, ?)", novo_funcionario)
conn.commit()

# Consultar e exibir funcionarios 
cursor.execute("SELECT * FROM funcionarios2")
funcionarios2 = cursor.fetchall()
print("Funcionários Cadastrados:")
for funcionario in funcionarios2:

    print(funcionario)

# Atualizando informacoes de um funcionario
atualizacao = ("Joao Silva", 5500.00, 1)
cursor.execute("UPDATE funcionarios2 SET nome = ?, salario = ?, WHERE id = ?", atualizacao)
conn.commit()

# Deletando um funcionario da tabela
id_funcionario_para_deletar = 1
cursor.execute("DELETE FROM funcionarios2 WHERE id = ?", (id_funcionario_para_deletar,))
conn.commit()