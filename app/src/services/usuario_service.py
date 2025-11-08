from db.queries import fetch, fetch_all, execute

def criar_usuario(nip, nome):
    sql = """
        INSERT INTO Usuario (nip, nome)
        VALUES (%s, %s)
        RETURNING id;
    """
    return fetch(sql, (nip, nome))[0]

def buscar_usuario_por_nip(nip):
    sql = "SELECT * FROM Usuario WHERE nip = %s;"
    return fetch(sql, (nip,))