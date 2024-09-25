# Excluir produto
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# ID do produto a ser excluido
produto_id = 1   

# Comando SQL para excluir produto
excluir_produto = "DELETE FROM Produtos WHERE id = ?"

# Executando o comando SQL de exclusao
cursor.execute(excluir_produto, (produto_id,))

# Confirmando as alteracoes
conn.commit()

# Fechando a conexao
conn.close()