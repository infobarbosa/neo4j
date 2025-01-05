from neo4j import GraphDatabase
import os
import csv

# Configuração do Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "SuperSenha123"

# Caminho dos arquivos CSV
CSV_DIR = "/home/barbosa/labs/bases-empresas/extracted"

# Estrutura do mapeamento de arquivos e tipos
FILE_MAPPINGS = {
    "Empresas": {
        "files": [f"Empresas{i}.csv" for i in range(10)],
        "query": """
        UNWIND $rows AS row
        MERGE (e:Empresa {cnpj_base: row[0]})
        SET e.razao_social = row[1],
            e.natureza_juridica = row[2],
            e.porte = row[3],
            e.capital_social = toFloat(replace(row[4], ',', '.')),
            e.situacao_cadastral = row[5];
        """
    },
    "Estabelecimentos": {
        "files": [f"Estabelecimentos{i}.csv" for i in range(10)],
        "query": """
        UNWIND $rows AS row
        MERGE (e:Estabelecimento {cnpj_base: row[0], ordem: row[1], dv: row[2]})
        SET e.identificador_matriz_filial = row[3],
            e.nome_fantasia = row[4],
            e.situacao_cadastral = row[5],
            e.data_situacao_cadastral = row[6],
            e.motivo_situacao_cadastral = row[7],
            e.nome_cidade_exterior = row[8],
            e.codigo_pais = row[9],
            e.data_inicio_atividade = row[10],
            e.cnae_fiscal = row[11],
            e.cnae_fiscal_secundario = row[12],
            e.tipo_logradouro = row[13],
            e.logradouro = row[14],
            e.numero = row[15],
            e.complemento = row[16],
            e.bairro = row[17],
            e.cep = row[18],
            e.uf = row[19],
            e.municipio = row[20],
            e.telefone1 = row[21],
            e.telefone2 = row[22],
            e.fax = row[23],
            e.email = row[24];
        """
    },
    "Socios": {
        "files": [f"Socios{i}.csv" for i in range(10)],
        "query": """
        UNWIND $rows AS row
        MERGE (s:Socio {cnpj_base: row[0], identificador_socio: row[1]})
        SET s.nome_socio = row[2],
            s.cpf_cnpj_socio = row[3],
            s.codigo_qualificacao_socio = row[4],
            s.data_entrada_sociedade = row[5],
            s.codigo_pais = row[6],
            s.cpf_representante = row[7],
            s.nome_representante = row[8],
            s.codigo_qualificacao_representante = row[9],
            s.faixa_etaria = row[10];
        """
    },
    "Motivos": {
        "files": ["Motivos.csv"],
        "query": """
        UNWIND $rows AS row
        MERGE (m:Motivo {codigo_motivo: row[0]})
        SET m.descricao = row[1];
        """
    },
    "Municipios": {
        "files": ["Municipios.csv"],
        "query": """
        UNWIND $rows AS row
        MERGE (m:Municipio {codigo_municipio: row[0]})
        SET m.descricao = row[1];
        """
    },
    "Naturezas": {
        "files": ["Naturezas.csv"],
        "query": """
        UNWIND $rows AS row
        MERGE (n:Natureza {codigo_natureza: row[0]})
        SET n.descricao = row[1];
        """
    },
    "Paises": {
        "files": ["Paises.csv"],
        "query": """
        UNWIND $rows AS row
        MERGE (p:Pais {codigo_pais: row[0]})
        SET p.descricao = row[1];
        """
    },
    "Qualificacoes": {
        "files": ["Qualificacoes.csv"],
        "query": """
        UNWIND $rows AS row
        MERGE (q:Qualificacao {codigo_qualificacao: row[0]})
        SET q.descricao = row[1];
        """
    },
}

# Função para limpar dados (remover caracteres inválidos)
def clean_row(row):
    return [col.replace('"', '').replace("\\", "") if col else None for col in row]

# Função para carregar os dados no Neo4j
def load_data_to_neo4j(driver, file_path, query):
    print(f"Carregando arquivo: {file_path}")
    rows = []
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            rows.append(clean_row(row))
    with driver.session() as session:
        session.run(query, rows=rows)

# Main script
def main():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    for entity, config in FILE_MAPPINGS.items():
        for file_name in config["files"]:
            file_path = os.path.join(CSV_DIR, file_name)
            if os.path.exists(file_path):
                load_data_to_neo4j(driver, file_path, config["query"])
            else:
                print(f"Arquivo não encontrado: {file_path}")
    driver.close()

if __name__ == "__main__":
    main()
