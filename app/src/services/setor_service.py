from db.queries import fetch, fetch_all, execute

def criar_setor(nome, descricao=None):
    sql = """
        INSERT INTO Setor (nome, descricao)
        VALUES (%s, %s)
        ON CONFLICT (nome) DO NOTHING
        RETURNING id;
    """
    result = fetch(sql, (nome,descricao))
    return result['id'] if result else None

def listar_setores():
    sql = "SELECT id, nome, descricao FROM Setor ORDER BY nome;"
    return fetch_all(sql)

def buscar_setor(id_setor):
    sql = "SELECT * FROM Setor WHERE id = %s;"
    return fetch(sql, (id_setor,))

def atualizar_setor(id_setor, nome=None, descricao=None):
    sql = """
        UPDATE Setor
        SET nome = COALESCE(%s, nome),
            descricao = COALESCE(%s, descricao)
        WHERE id = %s
        RETURNING id;
    """
    return fetch(sql, (nome, descricao, id_setor))

def excluir_setor(id_setor):
    sql = "DELETE FROM Setor WHERE id = %s RETURNING id;"
    return fetch(sql, (id_setor,))
