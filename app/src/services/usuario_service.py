from db.queries import fetch, fetch_all, execute

def criar_usuario(nip, nome):
    sql = """
        INSERT INTO Usuario (nip, nome)
        VALUES (%s, %s)
        ON CONFLICT (nip) DO NOTHING
        RETURNING id;
    """
    return fetch(sql, (nip, nome))[0]

def listar_usuarios():
    sql = "SELECT id, nip, nome FROM Usuario ORDER BY nome;"
    return fetch_all(sql)

def buscar_usuario_por_nip(nip):
    sql = "SELECT * FROM Usuario WHERE nip = %s;"
    return fetch(sql, (nip,))

def atualizar_usuario(id_usuario, nip=None, nome=None):
    sql = """
        UPDATE Usuario
        SET nip = COALESCE(%s, nip),
            nome = COALESCE(%s, nome)
        WHERE id = %s
        RETURNING id;
    """
    return fetch(sql, (nip, nome, id_usuario))

def excluir_usuario(id_usuario):
    sql = "DELETE FROM Usuario WHERE id = %s RETURNING id;"
    return fetch(sql, (id_usuario,))
