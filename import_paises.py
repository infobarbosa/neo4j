from neo4j import GraphDatabase
import csv

# Configuração do Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "SuperSenha123"

# Caminho do arquivo CSV
CSV_FILE = "/home/barbosa/labs/bases-empresas/extracted/Paises.csv"

def clean_row(row):
    return [col.replace('"', '').replace("\\", "") if col else None for col in row]

def load_paises(driver):
    query = """
    UNWIND $rows AS row
    MERGE (p:Pais {codigo_pais: row[0]})
    SET p.descricao = row[1];
    """
    rows = []
    with open(CSV_FILE, "r", encoding="ISO-8859-1") as csvfile:  # Ajuste de codificação
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            rows.append(clean_row(row))
    with driver.session() as session:
        session.run(query, rows=rows)

def main():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    load_paises(driver)
    driver.close()

if __name__ == "__main__":
    main()
