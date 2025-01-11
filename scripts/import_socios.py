from neo4j import GraphDatabase
import csv
import os

# Configuração do Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "SuperSenha123"

# Caminho do diretório contendo os arquivos de Sócios
CSV_DIR = "/home/barbosa/labs/bases-empresas/extracted"
SOCIOS_FILES = [f"Socios{i}.csv" for i in range(10)]  # Socios0.csv, Socios1.csv, etc.

# Caminho para o arquivo de log de erros
ERROR_LOG_FILE = "socios_erros.log"

BATCH_SIZE = 2000  # Define o tamanho do batch para commits parciais

def create_constraints(driver):
    """
    Cria restrições de unicidade para garantir que cada sócio seja identificado exclusivamente.
    """
    constraints = [
        """
        CREATE CONSTRAINT unique_socio_cpf_cnpj IF NOT EXISTS
        FOR (s:Socio)
        REQUIRE (s.cpf_cnpj_socio, s.cnpj_base) IS UNIQUE;
        """,
        """
        CREATE CONSTRAINT unique_empresa_cnpj_base IF NOT EXISTS
        FOR (e:Empresa)
        REQUIRE e.cnpj_base IS UNIQUE;
        """
    ]
    with driver.session() as session:
        for constraint_query in constraints:
            session.run(constraint_query)

def log_error(error_message):
    """
    Registra mensagens de erro no arquivo de log.
    """
    with open(ERROR_LOG_FILE, "a") as log_file:
        log_file.write(error_message + "\n")

def load_socios_with_relationships(driver, file_path, batch_size):
    """
    Carrega os dados de um arquivo CSV para o banco de dados Neo4j em batches e cria relacionamentos.
    """
    query = """
    UNWIND $rows AS row
    MERGE (s:Socio {cpf_cnpj_socio: row[3], cnpj_base: row[0]})  // Identificadores únicos
    SET s.tipo = row[1],
        s.nome = row[2],
        s.qualificacao = row[4],
        s.data_entrada = row[5],
        s.cpf_representante = row[6],
        s.nome_representante = row[7],
        s.qualificacao_representante = row[8],
        s.faixa_etaria = row[9],
        s.codigo_pais = row[10],  // Novo campo para código do país
        s.codigo_qualificacao_socio = row[11]  // Novo campo para código de qualificação
    WITH s, row
    MATCH (e:Empresa {cnpj_base: row[0]})  // Encontra a empresa correspondente
    MERGE (s)-[:SOCIO_DE]->(e)
    WITH s, row
    MATCH (pais:Pais {codigo_pais: row[10]})  // Encontra o país correspondente
    MERGE (s)-[:ORIGEM]->(pais)
    WITH s, row
    MATCH (qualificacao:Qualificacao {codigo_qualificacao: row[11]})  // Encontra a qualificação correspondente
    MERGE (s)-[:QUALIFICADO_COMO]->(qualificacao);
    """
    rows = []
    total_processed = 0

    with open(file_path, "r", encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for line_number, row in enumerate(reader, start=1):
            try:
                rows.append(row)  # Adiciona a linha diretamente sem higienização
                if len(rows) >= batch_size:
                    # Executa o batch
                    with driver.session() as session:
                        session.run(query, rows=rows)
                    total_processed += len(rows)
                    print(f"{total_processed} sócios processados e relacionados até agora no arquivo {file_path}...")
                    rows = []  # Reseta o batch
            except Exception as e:
                # Loga o erro com o número da linha e os valores da linha
                error_message = f"Erro no arquivo {file_path}, linha {line_number}: {e}. Valores: {row}"
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

    # Importa os arquivos de Sócios e relaciona com Empresas
    for file_name in SOCIOS_FILES:
        file_path = os.path.join(CSV_DIR, file_name)
        if os.path.exists(file_path):
            print(f"Carregando arquivo: {file_name}")
            load_socios_with_relationships(driver, file_path, BATCH_SIZE)
        else:
            print(f"Arquivo não encontrado: {file_name}")
            log_error(f"Arquivo não encontrado: {file_name}")

    # Encerra a conexão com o Neo4j
    driver.close()
    print("Importação concluída com sucesso! Verifique o arquivo de log para erros.")

if __name__ == "__main__":
    main()
