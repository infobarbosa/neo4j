from flask import Flask, render_template, request
from neo4j import GraphDatabase
from pyvis.network import Network
import logging
app = Flask(__name__)

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)

# Configuração do Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "SuperSenha123"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def fetch_graph_data(cnpj_base):
    """
    Busca informações no Neo4j sobre os sócios e empresas relacionadas a um CNPJ.
    """
    query = """
    MATCH (empresa:Empresa {cnpj_base: $cnpj_base})<-[:SOCIO_DE]-(socio:Socio)
    RETURN empresa, socio
    """
    data = []
    with driver.session() as session:
        result = session.run(query, cnpj_base=cnpj_base)
        for record in result:
            empresa = record["empresa"]
            socio = record["socio"]
            data.append((empresa, socio))
    return data

def generate_graph(cnpj_base):
    """
    Gera o grafo utilizando Pyvis com os dados retornados do Neo4j.
    """
    data = fetch_graph_data(cnpj_base)
    logger.info(f"Data: {data}")

    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

    for empresa, socio in data:
        # Adiciona a empresa central
        net.add_node(empresa["cnpj_base"], label=f"Empresa: {empresa['razao_social']}", color="blue")

        # Adiciona o sócio e o relacionamento com a empresa central
        net.add_node(socio["cpf_cnpj_socio"], label=f"Socio: {socio['nome']}", color="green")
        net.add_edge(socio["cpf_cnpj_socio"], empresa["cnpj_base"], label="SOCIO_DE")

    net.set_options('''
    var options = {
      "nodes": {
        "borderWidth": 2,
        "size": 25
      },
      "edges": {
        "color": {
          "inherit": true
        },
        "smooth": false
      },
      "physics": {
        "enabled": true
      }
    }
    ''')
    return net

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cnpj_base = request.form.get("cnpj_base")
        if cnpj_base:
            graph = generate_graph(cnpj_base)
            graph_path = f"./static/graph_{cnpj_base}.html"
            graph.save_graph(graph_path)
            return render_template("graph.html", graph_path=graph_path)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
