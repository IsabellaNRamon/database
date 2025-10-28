# conexão com banco de dados 
# pip install mysql-connector-python para estabelecer a conexão

import mysql.connector
from mysql.connector import Error 

def conectar():
    try:
        dbconfig = {
            'host': '127.0.0.1',
            'user': 'senai',
            'password': '1234',
            'database': 'senai',
        }

        con = mysql.connector.connect(**dbconfig)
        if con.is_connected():
            print("Conexão bem-sucedida!")
        return con

    except Error as error:
        print('Não conectou! ' + str(error))
        return None


def create(con, estudante):
    cursor = con.cursor()
    query = '''INSERT INTO estudante (matricula, nome) VALUES (%s, %s);'''

    try:
        cursor.executemany(query, estudante)
        con.commit()
        print("Registro inserido com sucesso!")
    except Error as error:
        print('Erro ao inserir! ' + str(error))
    finally:
        cursor.close()
        con.close()
        print('\nConexão fechada!\n')


def read(con):
    cursor = con.cursor()
    query = '''SELECT * FROM estudante;'''

    try:
        cursor.execute(query)
        print('\n\t\t\t ** SENAI - LISTA DE CHAMADA ** ')
        print('\tMatricula\t|\tNome')
        for campo in cursor.fetchall():
            print(f'\t{campo[0]}\t|\t{campo[1]}')

    except Error as error:
        print('Erro ao ler dados! ' + str(error))
    finally:
        cursor.close()
        con.close()
        print('\nConexão fechada!\n')


def update(con, estudante):
    cursor = con.cursor()
    query = '''UPDATE estudante SET nome = %s WHERE matricula = %s;'''
    try:
        cursor.executemany(query, estudante)
        con.commit()
        print("Registro atualizado com sucesso!")
    except Error as error:
        print('Erro ao atualizar! ' + str(error))
    finally:
        cursor.close()
        con.close()
        print('\nConexão fechada!\n')


def delete(con, estudante):
    cursor = con.cursor()
    query = '''DELETE FROM estudante WHERE matricula = %s;'''
    try:
        cursor.execute(query, estudante)
        con.commit()
        print("Registro excluído com sucesso!")
    except Error as error:
        print('Erro ao deletar! ' + str(error))
    finally:
        cursor.close()
        con.close()
        print('\nConexão fechada!\n')


# --- TESTES ---

# Inserir um estudante
create(conectar(), [('12345', 'Pedro')])

# Ler tabela
read(conectar())

