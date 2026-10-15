import pytest
import sqlite3
from usuario_sistema import adicionar_usuario, buscar_usuario

@pytest.fixture

def db_connection():
    """
    Fixture que configura uma conexão com o banco de dados SQLite 
    temporário e garante a limpeza dos recursos após o teste
    """

    conn = sqlite3.connect(":memory") # Cria BD em memória
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE usuarios(
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE 
    )
    """
    )

    conn.commit()
    yield conn, cursor

    conn.close()

@pytest.mark.parametrize(
    "id, nome, email, esperado_nome",
    [
        (1, "Roxany", "roxanyhelena@gmail.com", "Roxany"),
        (2, "Yolimar", "yolimar@gmail.com", "Yolimar"),
        (3, "Lucas", "proxyserie4@yahoo.com.br", "Lucas")
    ]
)

@pytest.mark.unit # É só uma etiqueta. Sem registro no pytest.ini

def test_adicionar_usuario(db_connection, id, nome, email, esperado_nome):
    conn, cursor = db_connection

    adicionar_usuario(cursor, id, nome, email)

    resultado = buscar_usuario(cursor, email)

    assert resultado is not None

    assert resultado[1] == esperado_nome

    assert resultado[2] == email

@pytest.mark.integration
def test_buscar_usuario_com_email_inexistente(db_connection):
    conn, cursor = db_connection
    resultado = buscar_usuario(cursor, "naoexistente@example.com")
    assert resultado in None

@pytest.mark.slow
@pytest.mark.integration
def test_adicionr_e_buscar_varios_usurios(db_connection):
    import time
    conn, cursor = db_connection

def test_buscar_usuario_com_email_inexistente(db_connection):
    import time

    conn, cursor = db_connection

    for i in range(100):
        adicionar_usuario(cursor, i, f"User{i}", f"user{i}@example.com")
        # Insere UM usuário por iteração. As f-string
        # Substituem {i} pelo valor atual:
        # i=0 - id=0, nome="User0", email="user0@example"
        # i=1 - id=1, nome="User1", email="user1@example"

    conn.commit()
    # Confira TODAS as 100 inserções de uma vez

    # PAUSA
    time.sleep(2)

    for i in range(100):
        resultado = buscar_usuario(cursor, f"user{i}@example.com")
        assert resultado is not None

        assert resultado[1] == f"User{i}"
        assert resultado[2] == f"user{i}example.com"