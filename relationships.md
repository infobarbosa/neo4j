# Relacionamentos 

### **Relacionamentos entre as Entidades**

#### **1. Empresa -> Estabelecimento**
Relacionamento: `:POSSUI`  
- Uma **Empresa** pode possuir vários **Estabelecimentos**.
- O relacionamento é baseado no `cnpj_base` compartilhado.

```cypher
MATCH (empresa:Empresa), (estabelecimento:Estabelecimento)
WHERE empresa.cnpj_base = estabelecimento.cnpj_base
CREATE (empresa)-[:POSSUI]->(estabelecimento);
```

---

#### **2. Empresa -> Sócio**
Relacionamento: `:TEM_SOCIO`  
- Uma **Empresa** pode ter vários **Sócios**.
- O relacionamento é baseado no `cnpj_base`.

```cypher
MATCH (empresa:Empresa), (socio:Socio)
WHERE empresa.cnpj_base = socio.cnpj_base
CREATE (empresa)-[:TEM_SOCIO]->(socio);
```

---

#### **3. Estabelecimento -> Município**
Relacionamento: `:LOCALIZADO_EM`  
- Um **Estabelecimento** está localizado em um **Município**.
- O relacionamento é baseado no `codigo_municipio`.

```cypher
MATCH (estabelecimento:Estabelecimento), (municipio:Municipio)
WHERE estabelecimento.codigo_municipio = municipio.codigo_municipio
CREATE (estabelecimento)-[:LOCALIZADO_EM]->(municipio);
```

---

#### **4. Estabelecimento -> Natureza Jurídica**
Relacionamento: `:CLASSIFICADO_COMO`  
- Um **Estabelecimento** tem uma **Natureza Jurídica**.
- O relacionamento é baseado no `codigo_natureza`.

```cypher
MATCH (estabelecimento:Estabelecimento), (natureza:Natureza)
WHERE estabelecimento.natureza_juridica = natureza.codigo_natureza
CREATE (estabelecimento)-[:CLASSIFICADO_COMO]->(natureza);
```

---

#### **5. Sócio -> País**
Relacionamento: `:ORIGEM`  
- Um **Sócio** pode ter origem em um **País**.
- O relacionamento é baseado no `codigo_pais`.

```cypher
MATCH (socio:Socio), (pais:Pais)
WHERE socio.codigo_pais = pais.codigo_pais
CREATE (socio)-[:ORIGEM]->(pais);
```

---

#### **6. Sócio -> Qualificação**
Relacionamento: `:QUALIFICADO_COMO`  
- Um **Sócio** possui uma **Qualificação**.
- O relacionamento é baseado no `codigo_qualificacao`.

```cypher
MATCH (socio:Socio), (qualificacao:Qualificacao)
WHERE socio.codigo_qualificacao_socio = qualificacao.codigo_qualificacao
CREATE (socio)-[:QUALIFICADO_COMO]->(qualificacao);
```

---

#### **7. Empresa -> Situação Cadastral**
Relacionamento: `:SITUACAO`  
- Uma **Empresa** pode ter uma **Situação Cadastral** associada.
- O relacionamento é baseado no `codigo_motivo`.

```cypher
MATCH (empresa:Empresa), (motivo:Motivo)
WHERE empresa.situacao_cadastral = motivo.codigo_motivo
CREATE (empresa)-[:SITUACAO]->(motivo);
```

---

### **Resumo dos Relacionamentos**

| **Entidade Origem**  | **Entidade Destino**  | **Relacionamento**     |
|-----------------------|-----------------------|-------------------------|
| Empresa               | Estabelecimento      | `:POSSUI`              |
| Empresa               | Sócio                | `:TEM_SOCIO`           |
| Estabelecimento       | Município            | `:LOCALIZADO_EM`       |
| Estabelecimento       | Natureza Jurídica    | `:CLASSIFICADO_COMO`   |
| Sócio                 | País                 | `:ORIGEM`              |
| Sócio                 | Qualificação         | `:QUALIFICADO_COMO`    |
| Empresa               | Situação Cadastral   | `:SITUACAO`            |

---

### **Como Executar os Comandos**
1. **Execute Cada Comando no Neo4j Browser:**
   - Copie e cole cada comando no Neo4j Browser para criar os relacionamentos.

2. **Via Cypher-Shell:**
   - Execute os comandos diretamente no terminal. Exemplo:
     ```bash
     cypher-shell -u neo4j -p SuperSenha123 "MATCH (empresa:Empresa), (estabelecimento:Estabelecimento) WHERE empresa.cnpj_base = estabelecimento.cnpj_base CREATE (empresa)-[:POSSUI]->(estabelecimento);"
     ```

---

### **Validação**
Após criar os relacionamentos, valide os dados com consultas como:

- **Exibir Relacionamentos:**
   ```cypher
   MATCH (empresa:Empresa)-[rel]->(destino)
   RETURN empresa.cnpj_base, type(rel), destino
   LIMIT 10;
   ```

- **Contar Relacionamentos:**
   ```cypher
   MATCH ()-[rel]->()
   RETURN type(rel), COUNT(rel);
   ```

