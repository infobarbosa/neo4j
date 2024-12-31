
# Neo4j 
Author: Prof. Barbosa<br>
Contact: infobarbosa@gmail.com<br>
Github: [infobarbosa](https://github.com/infobarbosa)

## Objetivo
Este laboratório foi criado para introduzir conceitos de bancos de dados em grafo usando **Neo4j** com suporte a contêineres **Docker** e scripts em **Python**.

## Sumário
1. [Pré-Requisitos](#pré-requisitos)
2. [Subir o Neo4j com Docker](#subir-o-neo4j-com-docker)
3. [Exercício Básico](#exercício-básico)
4. [Exercício Avançado](#exercício-avançado)
5. [Consultando os Dados](#consultando-os-dados)
6. [Encerrando o Ambiente](#encerrando-o-ambiente)

---

## Pré-Requisitos

- **Docker** instalado (versão 20+ recomendada).
- **Docker Compose** (versão 1.28+ ou 2+).
- **Python 3** instalado, para executar os scripts de inserção e consulta.

## Ambiente 
Este laborarório pode ser executado em qualquer estação de trabalho.<br>
Recomendo, porém, a execução em Linux.<br>
Caso você não tenha um à sua disposição, existe a opção do AWS Cloud9: siga essas [instruções](Cloud9/README.md).

---

## Subir o Neo4j com Docker

Na raiz do projeto, rode:

```bash
docker compose up -d

```

Isso iniciará um contêiner com **Neo4j** acessível em:

- **Neo4j Browser**: http://localhost:7474  
  *Usuário/Senha padrão:* `neo4j/test`

- **Bolt** (conexão via driver Python): `bolt://localhost:7687`

---

## Exercício 1

1. **Objetivo**: Verificar se o ambiente está funcionando corretamente.

2. **Passos**:
   - Na pasta `scripts`, execute:
     ```bash
     python3 insert_data_1.py

     ```
     Isso criará algumas Pessoas (ex: *Maria Santos*) e Empresas (ex: *TechSolutions*) e relacionamentos simples (ex: `Maria Santos` -[:TRABALHA_PARA]-> `TechSolutions`).

   - Para verificar, abra o Neo4j Browser em http://localhost:7474, conecte-se com usuário `neo4j` e senha `test`.  
     Rode a consulta:
     ```cypher
     MATCH (n) RETURN n;

     ```
     Você deve ver nós e relacionamentos referentes ao cenário básico.

3. **Validação**: Se você conseguir visualizar no Neo4j Browser os nós e relacionamentos criados, o ambiente está **OK**.

---

## Exercício 2

Agora que o ambiente está pronto, vamos inserir um cenário mais complexo, com **múltiplas pessoas e empresas** e **mais de 10 níveis de relacionamentos**.

1. **Inserir dados avançados**:
   ```bash
   python3 insert_data_2.py
   
   ```
2. **Verificar no Neo4j Browser**:
   ```cypher
   MATCH (n) RETURN n;
   
   ```
   Você verá um conjunto maior de nós, incluindo relacionamentos como `TRABALHA_PARA`, `E_SOCIO_DE`, `TEM_CONTRATO_COM`, `E_CASADO_COM`, entre outros.

3. **Objetivo**:  
   - Entender como relacionamentos complexos podem formar cadeias de dependência ou parceria entre pessoas e empresas.  
   - Explorar queries que encontrem caminhos entre diferentes empresas ou pessoas.

### Exemplo de Query Avançada

Para descobrir quantos *saltos* existem entre uma pessoa e outra:

```cypher
MATCH path = shortestPath(
    (p1:Pessoa {nome: 'Maria Santos'})-[:E_IRMAO_DE|E_SOCIO_DE|TRABALHA_PARA|...*]-(p2:Pessoa {nome:'Eduardo Lima'})
)
RETURN path;
```

> Ajuste os rótulos de relacionamentos `(...)|(...)|(...)` de acordo com o que deseja percorrer e explorar.

---

## Consultando os Dados

Para executar as consultas via Python, rode:

```bash
python3 queries.py

```

Esse script irá:
- Listar Pessoas  
- Listar Empresas  
- Mostrar relacionamentos existentes

---

## Encerrando o Ambiente

Para parar e remover o contêiner do Neo4j, execute:

```bash
docker compose down

```


## Parabéns!

Você concluiu com sucesso o laboratório de armazenamento em grafos com Neo4J! 🎉
Espero que este exercício tenha proporcionado uma compreensão prática sobre o funcionamento do modelo de armazenamento baseado em grafos.
 