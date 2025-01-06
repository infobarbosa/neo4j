from neo4j import GraphDatabase
import csv
import os

# Configuração do Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "SuperSenha123"

# Caminho do diretório contendo os arquivos de Empresas
CSV_DIR = "/home/barbosa/labs/bases-empresas/extracted"
EMPRESA_FILES = [f"Empresas{i}.csv" for i in range(10)]  # Empresas0.csv, Empresas1.csv, etc.

# Caminho para o arquivo de log de erros
ERROR_LOG_FILE = "empresas_erros.log"

BATCH_SIZE = 2000  # Define o tamanho do batch para commits parciais

def clean_row(row):
    """
    Limpa caracteres especiais indesejados em uma linha de dados.
    """
    return [col.replace('"', '').replace("\\", "") if col else None for col in row]

def create_constraints(driver):
    """
    Cria restrições de unicidade para garantir que cada empresa tenha um CNPJ único.
    """
    constraint_query = """
    CREATE CONSTRAINT unique_empresa_cnpj_base IF NOT EXISTS
    FOR (e:Empresa)
    REQUIRE e.cnpj_base IS UNIQUE;
    """
    with driver.session() as session:
        session.run(constraint_query)

def log_error(error_message):
    """
    Registra mensagens de erro no arquivo de log.
    """
    with open(ERROR_LOG_FILE, "a") as log_file:
        log_file.write(error_message + "\n")

def load_empresas_in_batches(driver, file_path, batch_size):
    """
    Carrega os dados de um arquivo CSV para o banco de dados Neo4j em batches.
    """
    query = """
    UNWIND $rows AS row
    MERGE (e:Empresa {cnpj_base: row[0]})  // Identificador único
    SET e.razao_social = row[1],
        e.natureza_juridica = row[2],
        e.porte = row[3],
        e.capital_social = toFloat(replace(row[4], ',', '.')),
        e.situacao_cadastral = row[5];
    """
    rows = []
    total_processed = 0  # Contador para registros processados

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
                    print(f"{total_processed} empresas processados até agora no arquivo {file_path}...")  # Progresso
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
                print(f"{total_processed} registros processados no total.")
            except Exception as e:
                error_message = f"Erro ao processar batch final no arquivo {file_path}: {e}"
                print(error_message)  # Mensagem no console
                log_error(error_message)  # Registro no log

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

    # Importa os arquivos de Empresas
    for file_name in EMPRESA_FILES:
        file_path = os.path.join(CSV_DIR, file_name)
        if os.path.exists(file_path):
            print(f"Carregando arquivo: {file_name}")
            load_empresas_in_batches(driver, file_path, BATCH_SIZE)
        else:
            print(f"Arquivo não encontrado: {file_name}")
            log_error(f"Arquivo não encontrado: {file_name}")

    # Encerra a conexão com o Neo4j
    driver.close()
    print("Importação concluída com sucesso! Verifique o arquivo de log para erros.")

if __name__ == "__main__":
    main()
