from db.queries import fetch, fetch_all, execute

def criar_setor(nome, descricao=None):
    sql = """
        INSERT INTO Setor (nome, descricao)
        VALUES (%s, %s)
        RETURNING id;
    """
    return fetch(sql, (nome,descricao))[0]

def listar_setores():
    sql = "SELECT id, nome, descricao FROM Setor ORDER BY nome;"
    return fetch_all(sql)

def buscar_setor(id_setor):
    sql = "SELECT * FROM Setor WHERE id = %s;"
    return fetch(sql, (id_setor,))