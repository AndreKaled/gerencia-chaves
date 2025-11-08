from db.queries import fetch, fetch_all, execute

def criar_chave(codigo, setor_id, descricao=None):
    sql = """
        INSERT INTO Chave (codigo, descricao, setor_id)
        VALUES (%s, %s, %s)
        RETURNING id;
    """
    return fetch(sql, (codigo, descricao, setor_id))[0]

def listar_chaves_ativas():
    sql = """
        SELECT c.id, c.codigo, c.descricao, s.nome AS Setor
        FROM Chave c
        JOIN Setor s ON s.id = c.setor_id
        WHERE c.ativo = TRUE
        ORDER BY c.codigo;
    """
    return fetch_all(sql)

def chave_emprestada(chave_id):
    sql = """
        SELECT *
        FROM Emprestimo
        WHERE chave_id = %s
          AND data_entrada IS NULL;
    """
    return fetch(sql, (chave_id,))
