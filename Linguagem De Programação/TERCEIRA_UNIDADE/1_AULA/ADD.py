# Adicionando produto
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Dados do novo produto
novo_produto = ('Camiseta', 19.99, 50)

# Comando SQL para inserir o novo produto na tabela
inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"

# Executando comando SQL para insercao
cursor.execute(inserir_produto, novo_produto)

# Confirmando as alteracoes
conn.commit()

# Fechando a conexao
conn.close