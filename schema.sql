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
    tipo INT (1, 2, 3) NOT NULL,
    id_conta_origem INT,
    id_conta_destino INT,
    valor FLOAT NOT NULL,
    data_transacao DATE,
    FOREIGN KEY (id_conta_origem) REFERENCES conta(id),
    FOREIGN KEY (id_conta_destino) REFERENCES conta(id),
    CONSTRAINT check_deposit_accounts CHECK ((tipo = 1 AND id_conta_destino IS NOT NULL AND id_conta_origem IS NULL) OR
                                            (tipo = 2 AND id_conta_destino IS NULL AND id_conta_origem IS NOT NULL) OR
                                            (tipo = 3 AND id_conta_destino IS NOT NULL AND id_conta_origem IS NOT NULL))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DELIMITER $$
CREATE TRIGGER atualiza_saldo AFTER INSERT ON transacao
FOR EACH ROW
BEGIN
    IF (NEW.tipo = 1) THEN
        UPDATE conta SET saldo = saldo + NEW.valor WHERE id = NEW.id_conta_destino;
    ELSEIF (NEW.tipo = 2) THEN
        UPDATE conta SET saldo = saldo - NEW.valor WHERE id = NEW.id_conta_origem;
    ELSEIF (NEW.tipo = 3) THEN
        UPDATE conta SET saldo = saldo - NEW.valor WHERE id = NEW.id_conta_origem;
        UPDATE conta SET saldo = saldo + NEW.valor WHERE id = NEW.id_conta_destino;
    END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER validaConta BEFORE INSERT ON transacao
FOR EACH ROW
BEGIN
	DECLARE source_account_exists INT;
    DECLARE dest_account_exists INT;
    IF (NEW.tipo = 3) THEN

        SELECT COUNT(*) INTO source_account_exists FROM conta WHERE id = NEW.id_conta_origem;
        SELECT COUNT(*) INTO dest_account_exists FROM conta WHERE id = NEW.id_conta_destino;

        IF source_account_exists = 0 OR dest_account_exists = 0 THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'A conta de origem ou de destino e invalida para a transferencia.';
        END IF;
    ELSEIF (NEW.tipo = 2) THEN

        SELECT COUNT(*) INTO source_account_exists FROM conta WHERE id = NEW.id_conta_origem;

        IF source_account_exists = 0 THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'A conta de origem para o saque nao existe';
        END IF;
    ELSEIF (NEW.tipo = 1) THEN

        SELECT COUNT(*) INTO dest_account_exists FROM conta WHERE id = NEW.id_conta_destino;

        IF dest_account_exists = 0 THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'A conta de de destino para o deposito nao existe';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'A conta de de destino para o deposito nao existe';
    END IF;

END$$
DELIMITER ;
