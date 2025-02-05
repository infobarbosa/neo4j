from neo4j import GraphDatabase
import csv

NEO4J_URI = "bolt://localhost:7687"
CSV_FILE = "/home/barbosa/labs/bases-empresas/extracted/Municipios.csv"

def clean_row(row):
    return [col.replace('"', '').replace("\\", "") if col else None for col in row]

def create_constraints(driver):
    query = """
    CREATE CONSTRAINT IF NOT EXISTS ON (m:Municipio) ASSERT m.codigo_municipio IS UNIQUE;
    """
    with driver.session() as session:
        session.run(query)
        print("Constraint 'unique_municipio_codigo' criada ou já existente.")

def load_municipios(driver):
    query = """
    UNWIND $rows AS row
    MERGE (m:Municipio {codigo_municipio: row[0]})
    SET m.descricao = row[1];
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
    create_constraints(driver)
    load_municipios(driver)
    driver.close()

if __name__ == "__main__":
    main()
