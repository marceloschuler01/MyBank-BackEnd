CREATE DATABASE IF NOT EXISTS mybank;

USE mybank;

CREATE TABLE IF NOT EXISTS cliente(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(13) NOT NULL UNIQUE,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS endereco(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cep VARCHAR(10) NOT NULL,
    numero INT,
    complemento VARCHAR(255),
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS agencia (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS funcionario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(13) NOT NULL UNIQUE,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE,
    salario INT,
    id_agencia INT,
    FOREIGN KEY (id_agencia) REFERENCES agencia(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS conta(
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo INT,
    saldo FLOAT DEFAULT 0.0,
    id_cliente INT,
    id_agencia INT,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    FOREIGN KEY (id_agencia) REFERENCES agencia(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS transacao(
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_conta_origem INT NOT NULL,
    id_conta_destino INT NOT NULL,
    valor FLOAT NOT NULL,
    data_transacao DATE,
    FOREIGN KEY (id_conta_origem) REFERENCES conta(id),
    FOREIGN KEY (id_conta_destino) REFERENCES conta(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
