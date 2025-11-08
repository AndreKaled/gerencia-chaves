from db.queries import fetch, execute

def registrar_saida(chave_id, usuario_id):
    sql = """
        INSERT INTO Emprestimo (chave_id, usuario_id)
        VALUES (%s, %s)
        RETURNING id;
    """
    return fetch(sql, (chave_id, usuario_id))[0]

def registrar_entrada(emprestimo_id, conferido_por=None):
    sql = """
        UPDATE Emprestimo
        SET data_entrada = NOW(),
            conferido_por = %s
        WHERE id = %s AND data_entrada IS NULL
        RETURNING id;
    """
    return fetch(sql, (conferido_por, emprestimo_id))

def historico_chave(chave_id):
    sql = """
        SELECT e.id, u.nome, e.data_saida, e.data_entrada
        FROM Emprestimo e
        JOIN Usuario u ON u.id = e.usuario_id
        WHERE e.chave_id = %s
        ORDER BY e.data_saida DESC;
    """
    return fetch_all(sql, (chave_id,))