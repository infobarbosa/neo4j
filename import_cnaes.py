from neo4j import GraphDatabase
import csv

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "SuperSenha123"
CSV_FILE = "/home/barbosa/labs/bases-empresas/extracted/Cnaes.csv"

def clean_row(row):
    return [col.replace('"', '').replace("\\", "") if col else None for col in row]

def load_cnaes(driver):
    query = """
    UNWIND $rows AS row
    MERGE (c:Cnae {codigo_cnae: row[0]})
    SET c.descricao = row[1];
    """
    rows = []
    with open(CSV_FILE, "r", encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            rows.append(clean_row(row))
    with driver.session() as session:
        session.run(query, rows=rows)

def main():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    load_cnaes(driver)
    driver.close()

if __name__ == "__main__":
    main()
