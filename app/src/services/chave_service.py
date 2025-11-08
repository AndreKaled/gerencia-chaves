from db.queries import fetch, fetch_all, execute

def criar_chave(codigo, setor_id, descricao=None):
    sql = """
        INSERT INTO Chave (codigo, descricao, setor_id)
        VALUES (%s, %s, %s)
        ON CONFLICT (codigo) DO NOTHING
        RETURNING id;
    """
    return fetch(sql, (codigo, descricao, setor_id))[0]

def listar_chaves():
    sql = """
        SELECT c.id, c.codigo, c.descricao, s.nome AS setor, c.ativo
        FROM Chave c
        JOIN Setor s ON s.id = c.setor_id
        ORDER BY c.codigo;
    """
    return fetch_all(sql)

def listar_chaves_ativas():
    sql = """
        SELECT c.id, c.codigo, c.descricao, s.nome AS setor
        FROM Chave c
        JOIN Setor s ON s.id = c.setor_id
        WHERE c.ativo = TRUE
        ORDER BY c.codigo;
    """
    return fetch_all(sql)

def buscar_chave(id_chave):
    sql = "SELECT * FROM Chave WHERE id = %s;"
    return fetch(sql, (id_chave,))

def atualizar_chave(id_chave, codigo=None, descricao=None, setor_id=None, ativo=None):
    sql = """
        UPDATE Chave
        SET codigo = COALESCE(%s, codigo),
            descricao = COALESCE(%s, descricao),
            setor_id = COALESCE(%s, setor_id),
            ativo = COALESCE(%s, ativo)
        WHERE id = %s
        RETURNING id;
    """
    return fetch(sql, (codigo, descricao, setor_id, ativo, id_chave))

def excluir_chave(id_chave):
    sql = "DELETE FROM Chave WHERE id = %s RETURNING id;"
    return fetch(sql, (id_chave,))
