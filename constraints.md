
### **Restrições de Chave Única**

#### **1. Empresas**
Atributo único: `cnpj_base`  
Cada empresa é identificada pelo campo `cnpj_base`.

```cypher
CREATE CONSTRAINT unique_empresa_cnpj_base
FOR (e:Empresa)
REQUIRE e.cnpj_base IS UNIQUE;
```

---

#### **2. Estabelecimentos**
Atributo único: `cnpj_base` + `cnpj_ordem` + `cnpj_dv`  
Cada estabelecimento é identificado pelo CNPJ completo (base, ordem e dígito verificador).

```cypher
CREATE CONSTRAINT unique_estabelecimento_cnpj
FOR (e:Estabelecimento)
REQUIRE (e.cnpj_base, e.cnpj_ordem, e.cnpj_dv) IS UNIQUE;
```

---

#### **3. Sócios**
Atributo único: `cpf_cnpj_socio` + `cnpj_base`  
Um sócio é único para uma empresa com base no CPF ou CNPJ associado ao sócio.

```cypher
CREATE CONSTRAINT unique_socio_cpf_cnpj
FOR (s:Socio)
REQUIRE (s.cpf_cnpj_socio, s.cnpj_base) IS UNIQUE;
```

---

#### **4. Naturezas Jurídicas**
Atributo único: `codigo_natureza`  
Cada natureza jurídica tem um código único.

```cypher
CREATE CONSTRAINT unique_natureza_codigo
FOR (n:Natureza)
REQUIRE n.codigo_natureza IS UNIQUE;
```

---

#### **5. Municípios**
Atributo único: `codigo_municipio`  
Cada município é identificado por um código único.

```cypher
CREATE CONSTRAINT unique_municipio_codigo
FOR (m:Municipio)
REQUIRE m.codigo_municipio IS UNIQUE;
```

---

#### **6. Países**
Atributo único: `codigo_pais`  
Cada país tem um código único.

```cypher
CREATE CONSTRAINT unique_pais_codigo
FOR (p:Pais)
REQUIRE p.codigo_pais IS UNIQUE;
```

---

#### **7. Qualificações**
Atributo único: `codigo_qualificacao`  
Cada qualificação tem um código único.

```cypher
CREATE CONSTRAINT unique_qualificacao_codigo
FOR (q:Qualificacao)
REQUIRE q.codigo_qualificacao IS UNIQUE;
```

---

#### **8. Motivos**
Atributo único: `codigo_motivo`  
Cada motivo tem um código único.

```cypher
CREATE CONSTRAINT unique_motivo_codigo
FOR (m:Motivo)
REQUIRE m.codigo_motivo IS UNIQUE;
```

---

### **Como Executar os Comandos**
1. **Via Neo4j Browser:**
   - Cole cada comando no Neo4j Browser e execute-os um por vez.

2. **Via Cypher-Shell:**
   - Execute os comandos diretamente no terminal, exemplo:
     ```bash
     cypher-shell -u neo4j -p SuperSenha123 "CREATE CONSTRAINT unique_empresa_cnpj_base FOR (e:Empresa) REQUIRE e.cnpj_base IS UNIQUE;"
     ```

3. **Valide os Constrangimentos Criados:**
   - Após executar, verifique as restrições criadas:
     ```cypher
     SHOW CONSTRAINTS;
     ```
