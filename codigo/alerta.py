import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database= "lazydb",
    port=3306
)

print("Conectado ao banco!")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM alertas")

dados = cursor.fetchall()

print("Total de registros:", len(dados))
print("------------------------")

for linha in dados:
    print(linha)

cursor.close()
conexao.close()