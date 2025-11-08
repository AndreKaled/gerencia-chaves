-- estrutura para sistema de gerencia empréstimo de chaves para setores
-- projetado para postgres

CREATE TABLE Setor(
    id SERIAL PROMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT
);

CREATE TABLE Usuario(
    id SERIAL PRIMARY KEY,
    nip INTEGER NOT NULL UNIQUE,
    nome, TEXT NOT NULL
);

CREATE TABLE Chave(
    id SERIAL PRIMARY KEY,
    codigo TEXT NOT NULL UNIQUE, -- codigo fisico da chave
    descricao TEXT,
    setor_id INTEGER NOT NULL REFERENCES Setor(id),
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE Emprestimo(
    id SERIAL PRIMARY KEY,
    chave_id INTEGER NOT NULL REFERENCES Chave(id),
    usuario_id INTEGER NOT NULL REFERENCES Usuario(id),
    
    data_saida TIMESTAMP NOT NULL DEFAULT NOW(),
    data_entrada TIMESTAMP NULL,

    conferido_por INTEGER REFERENCES Usuario(id),
    observacoes TEXT -- para casos diferentes do padrao
);

-- regra de apenas um emprestimo aberto por chave
CREATE UNIQUE INDEX emprestimo_unico_aberto_por_chave
    ON Emprestimo(chave_id)
    WHERE data_entrada IS NULL;