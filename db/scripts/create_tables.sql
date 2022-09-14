CREATE TABLE ESCOLAS (
ID_ESCOLA VARCHAR(2) NOT NULL PRIMARY KEY,
NOME_ESCOLA VARCHAR(50) NOT NULL
);

CREATE TABLE RACAS (
ID_RACA VARCHAR(3) NOT NULL PRIMARY KEY,
NOME_RACA VARCHAR(20) NOT NULL,
NOME_HABILIDADE VARCHAR(50) NOT NULL,
DESCRICAO_HABILIDADE TEXT NOT NULL,
NOME_RESTRICAO VARCHAR(50) NOT NULL,
DESCRICAO_RESTRICAO TEXT NOT NULL
);

CREATE TABLE ASPIRACOES (
ID_ASPIRACAO VARCHAR(2) NOT NULL PRIMARY KEY,
NOME_ASPIRACAO VARCHAR(15) NOT NULL
);

CREATE TABLE CAMINHOS (
ID_CAMINHO VARCHAR(3) NOT NULL PRIMARY KEY,
NOME_CAMINHO VARCHAR(50) NOT NULL,
TIER TINYINT NOT NULL,
MAESTRIA VARCHAR(150) NOT NULL,
REQUISITOS VARCHAR(150) NOT NULL
);



