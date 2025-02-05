from neo4j import GraphDatabase
import csv

NEO4J_URI = "bolt://localhost:7687"
CSV_FILE = "/home/barbosa/labs/bases-empresas/extracted/Qualificacoes.csv"

def clean_row(row):
    return [col.replace('"', '').replace("\\", "") if col else None for col in row]

def create_constraint(driver):
    with driver.session() as session:
        session.run("CREATE CONSTRAINT IF NOT EXISTS ON (q:Qualificacao) ASSERT q.codigo_qualificacao IS UNIQUE")

def load_qualificacoes(driver):
    query = """
    UNWIND $rows AS row
    MERGE (q:Qualificacao {codigo_qualificacao: row[0]})
    SET q.descricao = row[1];
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
    load_qualificacoes(driver)
    driver.close()

if __name__ == "__main__":
    main()
