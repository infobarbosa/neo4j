from neo4j import GraphDatabase
import csv
import os
import sys

# Configuração do Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "SuperSenha123"

ERROR_LOG_FILE = "estabelecimentos_erros.log"
BATCH_SIZE = 500

def create_constraints(driver):
    query = """
    CREATE CONSTRAINT unique_estabelecimento_cnpj IF NOT EXISTS
    FOR (e:Estabelecimento)
    REQUIRE (e.cnpj_base, e.cnpj_ordem, e.cnpj_dv) IS UNIQUE;
    """
    with driver.session() as session:
        session.run(query)
        print("Constraint 'unique_estabelecimento_cnpj' criada ou já existente.")

def log_error(error_message):
    with open(ERROR_LOG_FILE, "a") as log_file:
        log_file.write(error_message + "\n")

def load_estabelecimentos_in_batches(driver, file_path, batch_size, start_position=0):
    query = (
        "UNWIND $rows AS row "
        "MERGE (e:Estabelecimento {cnpj_base: row[0], cnpj_ordem: row[1], cnpj_dv: row[2]}) "
        "SET e.identificador_matriz_filial = row[3], e.nome_fantasia = row[4], e.situacao_cadastral = row[5], "
        "e.data_situacao_cadastral = row[6], e.motivo_situacao_cadastral = row[7], e.nome_cidade_exterior = row[8], "
        "e.pais = row[9], e.data_inicio_atividade = row[10], e.cnae_fiscal_principal = row[11], "
        "e.cnae_fiscal_secundaria = row[12], e.tipo_logradouro = row[13], e.logradouro = row[14], e.numero = row[15], "
        "e.complemento = row[16], e.bairro = row[17], e.cep = row[18], e.uf = row[19], e.municipio = row[20], "
        "e.ddd_telefone_1 = row[21], e.ddd_telefone_2 = row[22], e.ddd_fax = row[23], e.email = row[24], "
        "e.natureza_juridica = row[25] "
        "WITH e, row "
        "OPTIONAL MATCH (natureza:Natureza {codigo_natureza: row[25]}) "
        "FOREACH (_ IN CASE WHEN natureza IS NOT NULL THEN [1] ELSE [] END | "
        "    MERGE (e)-[:CLASSIFICADO_COMO]->(natureza)) "
        "WITH e, row "
        "OPTIONAL MATCH (municipio:Municipio {codigo_municipio: row[20]}) "
        "FOREACH (_ IN CASE WHEN municipio IS NOT NULL THEN [1] ELSE [] END | "
        "    MERGE (e)-[:LOCALIZADO_EM]->(municipio)) "
        "WITH e, row "
        "OPTIONAL MATCH (empresa:Empresa {cnpj_base: row[0]}) "
        "FOREACH (_ IN CASE WHEN empresa IS NOT NULL THEN [1] ELSE [] END | "
        "    MERGE (empresa)-[:POSSUI]->(e));"
    )

    rows = []
    total_processed = 0

    with open(file_path, "r", encoding="ISO-8859-1", errors="replace") as csvfile:
        reader = csv.reader((line.replace("\x00", "") for line in csvfile), delimiter=";")
        for line_number, row in enumerate(reader, start=1):
            if line_number < start_position:
                continue  # Ignora as linhas anteriores à posição inicial
            try:
                rows.append(row)
                if len(rows) >= batch_size:
                    try:
                        with driver.session() as session:
                            session.run(query, rows=rows)
                        total_processed += len(rows)
                        print(f"{total_processed} registros processados até agora no arquivo {file_path}...")
                        rows = []
                    except Exception as batch_error:
                        error_message = f"Erro ao processar batch no arquivo {file_path}, última linha {line_number}: {batch_error}"
                        print(error_message)
                        log_error(error_message)
                        rows = []  # Limpa o batch problemático e continua
            except Exception as line_error:
                error_message = f"Erro no arquivo {file_path}, linha {line_number}: {line_error}. Valores: {row}"
                print(error_message)
                log_error(error_message)

        if rows:
            try:
                with driver.session() as session:
                    session.run(query, rows=rows)
                total_processed += len(rows)
                print(f"{total_processed} registros processados no total no arquivo {file_path}.")
            except Exception as final_batch_error:
                error_message = f"Erro ao processar batch final no arquivo {file_path}: {final_batch_error}"
                print(error_message)
                log_error(error_message)

    print(f"Importação concluída para o arquivo {file_path}. Total processado: {total_processed} registros.")

def main():
    if len(sys.argv) < 3:
        print("Uso: python3 import_estabelecimentos.py <arquivo> <linha_inicial>")
        sys.exit(1)

    file_path = sys.argv[1]
    start_position = int(sys.argv[2])

    if not os.path.exists(file_path):
        print(f"Arquivo {file_path} não encontrado.")
        sys.exit(1)

    if os.path.exists(ERROR_LOG_FILE):
        os.remove(ERROR_LOG_FILE)

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    print("Criando restrições de unicidade...")
    create_constraints(driver)

    print(f"Carregando arquivo: {file_path} a partir da linha {start_position}...")
    load_estabelecimentos_in_batches(driver, file_path, BATCH_SIZE, start_position)

    driver.close()
    print("Importação concluída com sucesso! Verifique o arquivo de log para erros.")

if __name__ == "__main__":
    main()
