from db.connection import db

from services.setor_service import criar_setor
from services.usuario_service import criar_usuario
from services.chave_service import criar_chave
from services.emprestimo_service import registrar_saida

def main():
    print("Conectando ao banco...")
    db.connect()

    sid = criar_setor("Piscina", "Setor de psicsicanifna")
    uid = criar_usuario(123456, "Fulano da Silva")
    cid = criar_chave("CH-101", sid)

    emprestimo_id = registrar_saida(cid, uid)
    print("Empréstimo criado:", emprestimo_id)

    db.close()

if __name__ == "__main__":
    main()
