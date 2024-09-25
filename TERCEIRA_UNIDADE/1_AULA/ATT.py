# Atualizar o produto 
import sqlite3

conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Novo preco e ID do produto a ser atualizado
novo_preco = 24.99
produto_id = 1    # Suponhamos que queremos atualizar o produto com ID 1

# Comando SQL para atualizar o preco do produto
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"

# Executar o comando SQL de atualizacao
cursor.execute(atualizar_preco, (novo_preco, produto_id))

# Confirmando as alteracoes
conn.commit()

# Fechando a conexao
conn.close()