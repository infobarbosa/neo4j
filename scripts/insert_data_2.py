"""
insert_advanced_data.py

Cenário avançado com relações entre Pessoas e Empresas,
incluindo um encadeamento de pelo menos 10 níveis.
"""

from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "test"

def insert_advanced_data():
    # Exemplo (combina pessoas e empresas em português, criando relacionamentos complexos):
    # - Pessoas
    # - Empresas
    # - Relacionamentos com pelo menos 10 níveis em cadeia
    queries = [
        "CREATE (m:Pessoa {nome:'Maria Santos'})",
        "CREATE (j:Pessoa {nome:'João Silva'})",
        "CREATE (a:Pessoa {nome:'Ana Silva'})",
        "CREATE (p:Pessoa {nome:'Pedro Fonseca'})",
        "CREATE (c:Pessoa {nome:'Carla Ramos'})",
        "CREATE (r:Pessoa {nome:'Roberto Costa'})",
        "CREATE (f:Pessoa {nome:'Fernanda Oliveira'})",
        "CREATE (d:Pessoa {nome:'Daniel Souza'})",
        "CREATE (al:Pessoa {nome:'Aline Gomes'})",
        "CREATE (ed:Pessoa {nome:'Eduardo Lima'})",

        # Empresas
        "CREATE (tech:Empresa {nome:'TechSolutions'})",   # A
        "CREATE (agro:Empresa {nome:'AgroPlus'})",        # B
        "CREATE (fin:Empresa {nome:'FinanceCorp'})",      # C
        "CREATE (log:Empresa {nome:'LogisticaX'})",       # D
        "CREATE (cons:Empresa {nome:'ConsultoriaAvancada'})",  # Extra
        "CREATE (inov:Empresa {nome:'InovacaoTec'})",     # Extra
        "CREATE (sol:Empresa {nome:'SolucionaRH'})",      # Extra
        "CREATE (edu:Empresa {nome:'EducaBrasil'})",      # Extra

        # Relacionamentos (inspirados no exemplo):
        # Pessoa 1 trabalha para Empresa A
        "MATCH (m:Pessoa {nome:'Maria Santos'}), (tech:Empresa {nome:'TechSolutions'}) "
        "CREATE (m)-[:TRABALHA_PARA]->(tech)",

        # Pessoa 2 é sócia da Empresa A
        "MATCH (j:Pessoa {nome:'João Silva'}), (tech:Empresa {nome:'TechSolutions'}) "
        "CREATE (j)-[:E_SOCIO_DE]->(tech)",

        # Pessoa 3 é sócia da Empresa A
        "MATCH (a:Pessoa {nome:'Ana Silva'}), (tech:Empresa {nome:'TechSolutions'}) "
        "CREATE (a)-[:E_SOCIA_DE]->(tech)",

        # Pessoa 4 é sócia da Empresa B
        "MATCH (p:Pessoa {nome:'Pedro Fonseca'}), (agro:Empresa {nome:'AgroPlus'}) "
        "CREATE (p)-[:E_SOCIO_DE]->(agro)",

        # Pessoa 5 é diretora da empresa B
        "MATCH (c:Pessoa {nome:'Carla Ramos'}), (agro:Empresa {nome:'AgroPlus'}) "
        "CREATE (c)-[:E_DIRETORA_DE]->(agro)",

        # Pessoa 6 trabalha na empresa B
        "MATCH (r:Pessoa {nome:'Roberto Costa'}), (agro:Empresa {nome:'AgroPlus'}) "
        "CREATE (r)-[:TRABALHA_PARA]->(agro)",

        # Pessoa 7 trabalha para a empresa B
        "MATCH (f:Pessoa {nome:'Fernanda Oliveira'}), (agro:Empresa {nome:'AgroPlus'}) "
        "CREATE (f)-[:TRABALHA_PARA]->(agro)",

        # Pessoa 8 é casada com a Pessoa 1
        "MATCH (d:Pessoa {nome:'Daniel Souza'}), (m:Pessoa {nome:'Maria Santos'}) "
        "CREATE (d)-[:E_CASADO_COM]->(m)",

        # Pessoa 9 é filha da Pessoa 1
        "MATCH (al:Pessoa {nome:'Aline Gomes'}), (m:Pessoa {nome:'Maria Santos'}) "
        "CREATE (al)-[:E_FILHA_DE]->(m)",

        # Pessoa 9 trabalha para a empresa C
        "MATCH (al:Pessoa {nome:'Aline Gomes'}), (fin:Empresa {nome:'FinanceCorp'}) "
        "CREATE (al)-[:TRABALHA_PARA]->(fin)",

        # Pessoa 4 é sócia da empresa C
        "MATCH (p:Pessoa {nome:'Pedro Fonseca'}), (fin:Empresa {nome:'FinanceCorp'}) "
        "CREATE (p)-[:E_SOCIO_DE]->(fin)",

        # Empresa B é sócia da empresa C
        "MATCH (agro:Empresa {nome:'AgroPlus'}), (fin:Empresa {nome:'FinanceCorp'}) "
        "CREATE (agro)-[:E_SOCIA_DE]->(fin)",

        # Empresa D é sócia da empresa C
        "MATCH (log:Empresa {nome:'LogisticaX'}), (fin:Empresa {nome:'FinanceCorp'}) "
        "CREATE (log)-[:E_SOCIA_DE]->(fin)",

        # Empresa A tem contrato de prestação de serviços para a empresa C
        "MATCH (tech:Empresa {nome:'TechSolutions'}), (fin:Empresa {nome:'FinanceCorp'}) "
        "CREATE (tech)-[:TEM_CONTRATO_COM]->(fin)",

        # Vamos criar um encadeamento de 10 níveis, mostrando o potencial de grafos
        # 1) Daniel Souza -> É_IRMAO_DE -> Eduardo Lima
        "MATCH (d:Pessoa {nome:'Daniel Souza'}), (ed:Pessoa {nome:'Eduardo Lima'}) "
        "CREATE (d)-[:E_IRMAO_DE]->(ed)",

        # 2) Eduardo Lima -> É_SÓCIO_DE -> InovacaoTec
        "MATCH (ed:Pessoa {nome:'Eduardo Lima'}), (inov:Empresa {nome:'InovacaoTec'}) "
        "CREATE (ed)-[:E_SOCIO_DE]->(inov)",

        # 3) InovacaoTec -> TEM_CONTRATO_COM -> SolucionaRH
        "MATCH (inov:Empresa {nome:'InovacaoTec'}), (sol:Empresa {nome:'SolucionaRH'}) "
        "CREATE (inov)-[:TEM_CONTRATO_COM]->(sol)",

        # 4) SolucionaRH -> E_SOCIA_DE -> AgroPlus
        "MATCH (sol:Empresa {nome:'SolucionaRH'}), (agro:Empresa {nome:'AgroPlus'}) "
        "CREATE (sol)-[:E_SOCIA_DE]->(agro)",

        # 5) AgroPlus -> E_SOCIA_DE -> FinanceCorp
        # (já existe esse relacionamento, mas repetimos para fins de "cadeia" conceitual)
        # Em Neo4j, se tentarmos duplicar, ou fará duplicado ou não criará. Vamos "merge" ou criar outro rótulo.
        # Para simplificar, iremos apenas ressaltar que já existe esse passo na cadeia. (Sem duplicar.)

        # 6) FinanceCorp -> E_SOCIA_DE -> LogisticaX
        # (também já existe, iremos pular)

        # 7) LogisticaX -> E_FORNECEDORA_DE -> TechSolutions (exemplo)
        "MATCH (log:Empresa {nome:'LogisticaX'}), (tech:Empresa {nome:'TechSolutions'}) "
        "CREATE (log)-[:E_FORNECEDORA_DE]->(tech)",

        # 8) TechSolutions -> E_PARCEIRA_DE -> ConsultoriaAvancada
        "MATCH (tech:Empresa {nome:'TechSolutions'}), (cons:Empresa {nome:'ConsultoriaAvancada'}) "
        "CREATE (tech)-[:E_PARCEIRA_DE]->(cons)",

        # 9) ConsultoriaAvancada -> E_SOCIA_DE -> EducaBrasil
        "MATCH (cons:Empresa {nome:'ConsultoriaAvancada'}), (edu:Empresa {nome:'EducaBrasil'}) "
        "CREATE (cons)-[:E_SOCIA_DE]->(edu)",

        # 10) EducaBrasil -> E_SUBSIDIARIA_DE -> FinanceCorp
        "MATCH (edu:Empresa {nome:'EducaBrasil'}), (fin:Empresa {nome:'FinanceCorp'}) "
        "CREATE (edu)-[:E_SUBSIDIARIA_DE]->(fin)"
    ]

    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    with driver.session() as session:
        for q in queries:
            session.run(q)
    driver.close()
    print("Cenário avançado inserido com sucesso!")

if __name__ == "__main__":
    insert_advanced_data()