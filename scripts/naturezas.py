from neo4j import GraphDatabase
import csv

NEO4J_URI = "bolt://localhost:7687"
CSV_FILE = "/home/barbosa/labs/bases-empresas/extracted/Naturezas.csv"

def clean_row(row):
    return [col.replace('"', '').replace("\\", "") if col else None for col in row]

def create_constraint(driver):
    with driver.session() as session:
        session.run("CREATE CONSTRAINT IF NOT EXISTS ON (n:Natureza) ASSERT n.codigo_natureza IS UNIQUE")
    
def load_naturezas(driver):
    query = """
    UNWIND $rows AS row
    MERGE (n:Natureza {codigo_natureza: row[0]})
    SET n.descricao = row[1];
    """
    rows = []
    with open(CSV_FILE, "r", encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            rows.append(clean_row(row))
    with driver.session() as session:
        session.run(query, rows=rows)

def main():
    driver = GraphDatabase.driver(NEO4J_URI)
    create_constraint(driver)
    load_naturezas(driver)
    driver.close()

if __name__ == "__main__":
    main()
