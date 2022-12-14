import mysql.connector
import control.parser as parser

config = {
    'user': 'root',
    'password': 'Kvothe1807',
    'host': 'localhost',
    'database': 'alther_battleground',
    'raise_on_warnings': True
}


# Connection with the database
def open_connection():
    mydb = mysql.connector.connect(**config)
    return mydb


def create_cursor(connection):
    cursor = connection.cursor()
    return cursor


def close_connection(cursor, connection):
    cursor.close()
    connection.close()


# Character queries
def get_character_by_id(char_id):
    query = "SELECT detalhes FROM personagens WHERE id_personagem = %s"
    val = (char_id,)
    connection = open_connection()
    cursor = create_cursor(connection)

    cursor.execute(query, val)

    result = parser.parse_character_json(cursor.fetchone()[0], char_id)

    close_connection(cursor, connection)

    return result


def save_new_character(char_json):
    query = "INSERT INTO personagens (detalhes) VALUES (%s)"
    val = (char_json,)
    connection = open_connection()
    cursor = create_cursor(connection)

    cursor.execute(query, val)
    connection.commit()

    close_connection(cursor, connection)

    print("Personagem salvo.")


def update_existing_character(char_id, char_json):
    query = "UPDATE personagens SET detalhes = %s WHERE id_personagem = %s"
    val = (char_json, char_id)
    connection = open_connection()
    cursor = create_cursor(connection)

    cursor.execute(query, val)
    connection.commit()

    close_connection(cursor, connection)

    print("Personagem atualizado.")


def delete_existing_character(char_id):
    query = "DELETE FROM personagens WHERE id_personagem = %s"
    val = (char_id,)
    connection = open_connection()
    cursor = create_cursor(connection)

    cursor.execute(query, val)
    connection.commit()

    close_connection(cursor, connection)

    print("Personagem deletado.")


def get_all_characters():
    query = "SELECT * FROM personagens"

    connection = open_connection()
    cursor = create_cursor(connection)

    cursor.execute(query)

    r = cursor.fetchall()

    close_connection(cursor, connection)

    return [parser.parse_character_json(det, char_id) for char_id, det in r]


# Skills queries
def get_all_skills():
    query = "SELECT * FROM habilidades"

    connection = open_connection()
    cursor = create_cursor(connection)

    cursor.execute(query)

    r = cursor.fetchall()

    close_connection(cursor, connection)

    return [parser.parse_skill(response) for response in r]

