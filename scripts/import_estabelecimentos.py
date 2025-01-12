from neo4j import GraphDatabase
import csv
import os

# Configuração do Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "SuperSenha123"

# Caminho do diretório contendo os arquivos de Estabelecimentos
CSV_DIR = "/home/barbosa/labs/bases-empresas/extracted"
ESTABELECIMENTO_FILES = [f"Estabelecimentos{i}.csv" for i in range(10)]  # Estabelecimentos0.csv, Estabelecimentos1.csv, etc.

# Caminho para o arquivo de log de erros
ERROR_LOG_FILE = "estabelecimentos_erros.log"

BATCH_SIZE = 500  # Define o tamanho do batch para commits parciais

def clean_row(row):
    """
    Limpa caracteres especiais indesejados em uma linha de dados.
    """
    return [col.replace('"', '').replace("\\", "") if col else None for col in row]

def create_constraints(driver):
    """
    Cria restrições de unicidade para garantir que cada estabelecimento tenha um identificador único baseado em
    cnpj_base, cnpj_ordem e cnpj_dv.
    """
    constraint_name = "unique_estabelecimento_cnpj"
    check_constraint_query = f"""
    SHOW CONSTRAINTS WHERE name = '{constraint_name}'
    """
    create_constraint_query = f"""
    CREATE CONSTRAINT {constraint_name} IF NOT EXISTS
    FOR (e:Estabelecimento)
    REQUIRE (e.cnpj_base, e.cnpj_ordem, e.cnpj_dv) IS UNIQUE
    """
    with driver.session() as session:
        # Verifica se a constraint já existe
        existing_constraints = session.run(check_constraint_query)
        if any(row["name"] == constraint_name for row in existing_constraints):
            print(f"Constraint '{constraint_name}' já existe.")
        else:
            print(f"Criando constraint '{constraint_name}'...")
            session.run(create_constraint_query)
            print(f"Constraint '{constraint_name}' criada com sucesso.")

def log_error(error_message):
    """
    Registra mensagens de erro no arquivo de log.
    """
    with open(ERROR_LOG_FILE, "a") as log_file:
        log_file.write(error_message + "\n")

def load_estabelecimentos_in_batches(driver, file_path, batch_size):
    """
    Carrega os dados de um arquivo CSV para o banco de dados Neo4j em batches.
    """
    query = """
    UNWIND $rows AS row
    MERGE (e:Estabelecimento {cnpj_base: row[0], cnpj_ordem: row[1], cnpj_dv: row[2]})  // Identificador único
    SET e.identificador_matriz_filial = row[3],
        e.nome_fantasia = row[4],
        e.situacao_cadastral = row[5],
        e.data_situacao_cadastral = row[6],
        e.motivo_situacao_cadastral = row[7],
        e.nome_cidade_exterior = row[8],
        e.pais = row[9],
        e.data_inicio_atividade = row[10],
        e.cnae_fiscal_principal = row[11],
        e.cnae_fiscal_secundaria = row[12],
        e.tipo_logradouro = row[13],
        e.logradouro = row[14],
        e.numero = row[15],
        e.complemento = row[16],
        e.bairro = row[17],
        e.cep = row[18],
        e.uf = row[19],
        e.municipio = row[20],
        e.ddd_telefone_1 = row[21],
        e.ddd_telefone_2 = row[22],
        e.ddd_fax = row[23],
        e.email = row[24],
        e.natureza_juridica = row[25];  // Adiciona natureza_juridica
    WITH e, row
    MATCH (natureza:Natureza {codigo_natureza: row[25]})
    CREATE (e)-[:CLASSIFICADO_COMO]->(natureza);
    """
    rows = []
    total_processed = 0  # Contador para registros processados
    file_processed = 0  # Contador para o arquivo atual

    with open(file_path, "r", encoding="ISO-8859-1") as csvfile:  # Ajuste de codificação
        reader = csv.reader(csvfile, delimiter=";")
        for line_number, row in enumerate(reader, start=1):
            try:
                rows.append(clean_row(row))  # Limpeza de caracteres
                if len(rows) >= batch_size:
                    # Executa o batch
                    with driver.session() as session:
                        session.run(query, rows=rows)
                    total_processed += len(rows)
                    file_processed += len(rows)
                    print(f"{file_processed} registros processados do arquivo {file_path}...")  # Progresso
                    rows = []  # Reseta o batch
            except Exception as e:
                # Loga o erro com o número da linha
                error_message = f"Erro no arquivo {file_path}, linha {line_number}: {e}"
                print(error_message)  # Mensagem no console
                log_error(error_message)  # Registro no log

        # Processa os registros restantes
        if rows:
            try:
                with driver.session() as session:
                    session.run(query, rows=rows)
                total_processed += len(rows)
                file_processed += len(rows)
                print(f"{file_processed} registros processados do arquivo {file_path} no total.")
            except Exception as e:
                error_message = f"Erro ao processar batch final no arquivo {file_path}: {e}"
                print(error_message)  # Mensagem no console
                log_error(error_message)  # Registro no log

    print(f"Importação concluída para o arquivo {file_path}. Total processado: {file_processed} registros.")

def main():
    """
    Função principal para executar o fluxo de importação.
    """
    # Remove o log anterior (se existir)
    if os.path.exists(ERROR_LOG_FILE):
        os.remove(ERROR_LOG_FILE)

    # Inicializa o driver do Neo4j
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    # Cria restrições de unicidade
    print("Criando restrições de unicidade...")
    create_constraints(driver)

    # Importa os arquivos de Estabelecimentos
    for file_name in ESTABELECIMENTO_FILES:
        file_path = os.path.join(CSV_DIR, file_name)
        if os.path.exists(file_path):
            print(f"Carregando arquivo: {file_name}")
            load_estabelecimentos_in_batches(driver, file_path, BATCH_SIZE)
        else:
            print(f"Arquivo não encontrado: {file_name}")
            log_error(f"Arquivo não encontrado: {file_name}")

    # Encerra a conexão com o Neo4j
    driver.close()
    print("Importação concluída com sucesso! Verifique o arquivo de log para erros.")

if __name__ == "__main__":
    main()
