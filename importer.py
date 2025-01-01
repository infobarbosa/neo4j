from neo4j import GraphDatabase
import csv
import glob

# Configurações de conexão com o Neo4j
URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "SuperSenha123"

class Neo4jImporter:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def clear_label(self, label):
        with self.driver.session() as session:
            try:
                print(f"Limpando dados do label {label}...")
                session.run(f"MATCH (n:{label}) DETACH DELETE n")
            except Exception as e:
                print(f"Erro ao limpar o label {label}: {e}")

    def load_csv_to_neo4j(self, file_path, query):
        with self.driver.session() as session:
            try:
                with open(file_path, encoding='utf-8', errors='replace') as csv_file:
                    reader = csv.reader(csv_file, delimiter=';')
                    next(reader)  # Pula o cabeçalho
                    for line_number, row in enumerate(reader, start=2):  # Inicia a contagem das linhas após o cabeçalho
                        try:
                            session.run(query, {"row": row})
                        except Exception as e:
                            print(f"Erro ao processar a linha {line_number} no arquivo {file_path}: {e}")
            except UnicodeDecodeError as e:
                print(f"Erro de codificação ao ler o arquivo {file_path}: {e}")
            except Exception as e:
                print(f"Erro inesperado ao processar o arquivo {file_path}: {e}")

# Queries de carregamento
QUERIES = {
    "Empresas": """
        CREATE (e:Empresa {
            id: toInteger($row[0]),
            nome: $row[1],
            cnae: $row[2],
            tipo: $row[3],
            capital: toFloat($row[4]),
            porte: $row[5]
        });
    """,
    "Estabelecimentos": """
        CREATE (es:Estabelecimento {
            id: toInteger($row[0]),
            cnpj: $row[1],
            tipo: $row[2],
            situacao: $row[3],
            logradouro: $row[15],
            numero: $row[16],
            bairro: $row[18],
            cep: $row[19],
            uf: $row[20],
            email: $row[29]
        });
    """,
    "Socios": """
        CREATE (s:Socio {
            id: toInteger($row[0]),
            tipo: $row[1],
            nome: $row[2],
            cpf_cnpj: $row[3],
            qualificacao: $row[4],
            entrada: $row[5]
        });
    """,
    "Qualificacoes": """
        CREATE (q:Qualificacao {
            codigo: $row[0],
            descricao: $row[1]
        });
    """,
    "Paises": """
        CREATE (p:Pais {
            codigo: $row[0],
            nome: $row[1]
        });
    """,
    "Naturezas": """
        CREATE (n:Natureza {
            codigo: $row[0],
            descricao: $row[1]
        });
    """,
    "Municipios": """
        CREATE (m:Municipio {
            codigo: $row[0],
            nome: $row[1]
        });
    """,
    "Motivos": """
        CREATE (mt:Motivo {
            codigo: $row[0],
            descricao: $row[1]
        });
    """
}

# Caminho para os arquivos
BASE_DIR = "/home/barbosa/labs/bases-empresas/extracted/"

# Mapeamento dos arquivos para seus respectivos labels
FILES = {
    "Empresas": glob.glob(f"{BASE_DIR}/Empresas*.csv"),
    "Estabelecimentos": glob.glob(f"{BASE_DIR}/Estabelecimentos*.csv"),
    "Socios": glob.glob(f"{BASE_DIR}/Socios*.csv"),
    "Qualificacoes": [f"{BASE_DIR}/Qualificacoes.csv"],
    "Paises": [f"{BASE_DIR}/Paises.csv"],
    "Naturezas": [f"{BASE_DIR}/Naturezas.csv"],
    "Municipios": [f"{BASE_DIR}/Municipios.csv"],
    "Motivos": [f"{BASE_DIR}/Motivos.csv"]
}

# Importação
importer = Neo4jImporter(URI, USERNAME, PASSWORD)

try:
    for label, file_paths in FILES.items():
        query = QUERIES[label]
        
        # Limpeza do label
        importer.clear_label(label)
        
        # Carregamento dos arquivos
        for file_path in file_paths:
            print(f"Carregando {file_path} no label {label}...")
            importer.load_csv_to_neo4j(file_path, query)
finally:
    importer.close()
    print("Importação concluída!")
