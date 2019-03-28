
import sqlite3

connection = sqlite3.connect('data_wei_pos_tim.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS dados (peso real, posicaolon float, posicaolat float , horario float)"
cursor.execute(create_table)

connection.commit()

connection.close()
