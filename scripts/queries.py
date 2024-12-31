"""
queries.py

Exemplos de consultas básicas no Neo4j:
 - Listar todas as pessoas
 - Listar todas as empresas
 - Exibir relacionamentos
"""

from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "test"

def run_queries():
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    with driver.session() as session:
        print("=== Pessoas ===")
        result = session.run("MATCH (p:Pessoa) RETURN p.nome AS nome")
        for record in result:
            print(record["nome"])

        print("\n=== Empresas ===")
        result = session.run("MATCH (e:Empresa) RETURN e.nome AS nome")
        for record in result:
            print(record["nome"])
        
        print("\n=== Relacionamentos (com rótulo) ===")
        result = session.run("""
            MATCH (n)-[rel]->(m) 
            RETURN n.nome AS de, type(rel) AS relacao, m.nome AS para 
            ORDER BY de
        """)
        for record in result:
            print(f"{record['de']} -[:{record['relacao']}]-> {record['para']}")
    driver.close()

if __name__ == "__main__":
    run_queries()