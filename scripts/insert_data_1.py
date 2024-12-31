"""
insert_basic_data.py

Script de inserção de dados básicos em um banco Neo4j para fins de teste.
Exemplo de conexão e criação de nós e relacionamentos.
"""

from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "test"

def insert_basic_data():
    # Exemplo de cenário simples de Pessoas e Empresas
    # com alguns relacionamentos básicos.
    queries = [
        # Criar algumas pessoas (nós)
        "CREATE (m:Pessoa {nome:'Maria Santos'})",
        "CREATE (j:Pessoa {nome:'João Silva'})",
        "CREATE (l:Pessoa {nome:'Luana Costa'})",

        # Criar algumas empresas (nós)
        "CREATE (tech:Empresa {nome:'TechSolutions'})",
        "CREATE (fin:Empresa {nome:'FinanceCorp'})",

        # Relacionamentos básicos
        "MATCH (m:Pessoa {nome:'Maria Santos'}), (tech:Empresa {nome:'TechSolutions'}) "
        "CREATE (m)-[:TRABALHA_PARA]->(tech)",

        "MATCH (j:Pessoa {nome:'João Silva'}), (tech:Empresa {nome:'TechSolutions'}) "
        "CREATE (j)-[:E_SOCIO_DE]->(tech)",

        "MATCH (l:Pessoa {nome:'Luana Costa'}), (tech:Empresa {nome:'TechSolutions'}) "
        "CREATE (l)-[:E_SOCIA_DE]->(tech)",

        # Relação entre empresas
        "MATCH (tech:Empresa {nome:'TechSolutions'}), (fin:Empresa {nome:'FinanceCorp'}) "
        "CREATE (tech)-[:TEM_CONTRATO_COM]->(fin)"
    ]

    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    with driver.session() as session:
        for q in queries:
            session.run(q)
    driver.close()
    print("Dados básicos inseridos com sucesso!")

if __name__ == "__main__":
    insert_basic_data()