from flask import Flask, render_template, request
from neo4j import GraphDatabase
from pyvis.network import Network
from markupsafe import Markup

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

    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
    net.barnes_hut()

    for empresa, socio in data:
        # Adiciona a empresa central
        net.add_node(empresa["cnpj_base"], label=f"Empresa: {empresa['razao_social']}", color="#005CA9", shape="ellipse")

        # Adiciona o sócio e o relacionamento com a empresa central
        net.add_node(socio["cpf_cnpj_socio"], label=f"Socio: {socio['nome']}", color="#FF6A00", shape="circle")
        net.add_edge(socio["cpf_cnpj_socio"], empresa["cnpj_base"], label="SOCIO_DE")

    net.set_options('''
    var options = {
      "nodes": {
        "borderWidth": 2,
        "size": 30,
        "font": {
          "size": 14,
          "color": "white"
        }
      },
      "edges": {
        "width": 1,
        "font": {
          "size": 12,
          "color": "#dddddd"
        },
        "smooth": {
          "type": "continuous"
        }
      },
      "physics": {
        "barnesHut": {
          "gravitationalConstant": -30000,
          "centralGravity": 0.3,
          "springLength": 200,
          "springConstant": 0.04
        },
        "minVelocity": 0.75
      }
    }
    ''')
    return net.generate_html()

@app.route("/", methods=["GET", "POST"])
def index():
    graph_html = None
    cnpj_base = None

    if request.method == "POST":
        cnpj_base = request.form.get("cnpj_base")
        if cnpj_base:
            graph_html = Markup(generate_graph(cnpj_base))

    return render_template("index.html", graph_html=graph_html, cnpj_base=cnpj_base)

if __name__ == "__main__":
    app.run(debug=True)
