def adicionar_usuario(cursor, id, nome, email):
    """Adiciona um usuario ao banco de dados"""
    cursor.execute('''
    INSERT INTO usuario(id, nome, email)
    VALUES(?,?,?)
    ''', (id, nome, email))

def buscar_usuario(cursor, email):
    """Busca um usuario pelo e-mail"""
    cursor.execute("SELECT * FROM usuario WHERE email = ?",
                   (email, ))
    return cursor.fetchone()