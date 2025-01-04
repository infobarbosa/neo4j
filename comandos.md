
### **1. Especificar os Campos no Comando Cypher**
Supondo que as colunas do arquivo estejam no seguinte formato (sem cabeçalho):
```plaintext
"41273593";"JULIO CESAR NUNES 39611300867";"2135";"50";"3000,00";"01";""
```

E os campos correspondem a:
- `cnpj_base`
- `razao_social`
- `natureza_juridica`
- `porte`
- `capital_social`
- `situacao_cadastral`
- `outro`

Você pode carregar os dados assim:

```cypher
LOAD CSV FROM 'file:///empresas.csv' AS row
FIELDTERMINATOR ';'
CREATE (:Empresa {
  cnpj_base: row[0],
  razao_social: row[1],
  natureza_juridica: row[2],
  porte: row[3],
  capital_social: toFloat(replace(row[4], ',', '.')),
  situacao_cadastral: row[5]
});

```

---

### **2. Explicação do Comando**
- **`LOAD CSV FROM 'file:///empresas.csv'`**: Carrega o arquivo CSV sem cabeçalhos.
- **`AS row`**: Cada linha do arquivo é tratada como uma lista, e você acessa os valores pelas posições do índice (`row[0]`, `row[1]`, etc.).
- **`FIELDTERMINATOR ';'`**: Define `;` como delimitador de campos.
- **Conversão do `capital_social`**: O comando `replace(row[4], ',', '.')` substitui a vírgula decimal por um ponto para permitir a conversão em número com `toFloat`.

---

### **3. Verificar o Resultado**
Após executar o comando, verifique os dados carregados:

- **Visualizar alguns nós:**
  ```cypher
  MATCH (e:Empresa)
  RETURN e.cnpj_base, e.razao_social, e.capital_social
  LIMIT 10;
  ```

- **Contar os nós carregados:**
  ```cypher
  MATCH (e:Empresa)
  RETURN COUNT(e) AS total_empresas;
  ```

---

### **4. Alternativa: Adicionar Cabeçalhos ao Arquivo**
Se preferir, você pode adicionar manualmente um cabeçalho ao arquivo original ou criar um novo arquivo CSV com cabeçalho, como:

```plaintext
cnpj_base;razao_social;natureza_juridica;porte;capital_social;situacao_cadastral;outro
"41273593";"JULIO CESAR NUNES 39611300867";"2135";"50";"3000,00";"01";""
```

Assim, o carregamento pode ser feito usando `WITH HEADERS`.

---


```
LOAD CSV FROM 'file:///Empresas0.csv' AS row
FIELDTERMINATOR ';'
CREATE (:Empresa {
  cnpj_base: row[0],
  razao_social: row[1],
  natureza_juridica: row[2],
  porte: row[3],
  capital_social: toFloat(replace(row[4], ',', '.')),
  situacao_cadastral: row[5]
});

```

```cypher
:auto LOAD CSV FROM 'file:///Empresas1.csv' AS row FIELDTERMINATOR ';'
CALL {
    WITH row
    CREATE (:Empresa { 
        cnpj_base: row[0],
        razao_social: row[1],
        natureza_juridica: row[2],
        porte: row[3],
        capital_social: toFloat(replace(row[4], ',', '.')),
        situacao_cadastral: row[5]
    })
} IN TRANSACTIONS OF 200 ROWS;

```




Para deletar uma **label** no **Neo4j**, não é possível remover a label diretamente de todo o banco como um todo, pois as labels são propriedades intrínsecas associadas aos nós. No entanto, você pode **remover a label de um conjunto de nós** ou **deletar completamente os nós que possuem essa label**.

Aqui estão as duas abordagens possíveis:

---

### **1. Remover a Label de Todos os Nós `Empresa`**
Se deseja apenas remover a label `Empresa` de todos os nós que a possuem (sem deletar os nós):

```cypher
MATCH (e:Empresa)
REMOVE e:Empresa;
```

#### **O que acontece?**
- Os nós permanecerão no banco de dados, mas sem a label `Empresa`.
- Quaisquer outras labels ou propriedades associadas aos nós não serão afetadas.

---

### **2. Deletar os Nós com a Label `Empresa`**
Se deseja deletar todos os nós que possuem a label `Empresa`:

```cypher
MATCH (e:Empresa)
DETACH DELETE e;
```

#### **O que acontece?**
- Todos os nós com a label `Empresa` serão removidos, junto com quaisquer relacionamentos associados (graças ao `DETACH`).

---

### **3. Verificar Antes de Remover**
Antes de executar qualquer um dos comandos acima, você pode verificar os dados para ter certeza do impacto:

- Contar os nós com a label `Empresa`:
  ```cypher
  MATCH (e:Empresa)
  RETURN COUNT(e) AS total_empresas;
  ```

- Listar algumas amostras:
  ```cypher
  MATCH (e:Empresa)
  RETURN e LIMIT 10;
  ```

---

### **Considerações**
- Sempre tenha cuidado ao executar comandos de remoção, especialmente em bancos de produção.
- Se precisar de mais controle sobre a remoção (por exemplo, remover a label apenas de certos nós), você pode adicionar filtros no comando `MATCH`.

---

# Estabelecimentos

Para carregar os dados do arquivo `estabelecimentos.csv` no Neo4j como nós com a label `Estabelecimento`, considerando o **sample** e o **layout fornecido**, o comando seria o seguinte:

---

### **Comando de Carga**
```cypher
LOAD CSV FROM 'file:///estabelecimentos.csv' AS row
FIELDTERMINATOR ';'
CREATE (:Estabelecimento {
  cnpj_base: row[0],
  cnpj_ordem: row[1],
  cnpj_dv: row[2],
  matriz_filial: toInteger(row[3]),
  nome_fantasia: row[4],
  situacao_cadastral: row[5],
  data_situacao_cadastral: date(row[6]),
  motivo_situacao_cadastral: row[7],
  cidade_exterior: row[8],
  codigo_pais: row[9],
  data_inicio_atividade: date(row[10]),
  cnae_fiscal_principal: row[11],
  cnaes_secundarias: split(row[12], ','),
  tipo_logradouro: row[13],
  logradouro: row[14],
  numero: row[15],
  complemento: row[16],
  bairro: row[17],
  cep: row[18],
  uf: row[19],
  codigo_municipio: row[20],
  ddd_telefone1: row[21],
  telefone1: row[22],
  ddd_telefone2: row[23],
  telefone2: row[24],
  ddd_fax: row[25],
  fax: row[26],
  email: row[27],
  situacao_especial: row[28],
  data_situacao_especial: row[29]
});
```

---

### **Detalhes do Comando**
1. **`FIELDTERMINATOR ';'`**:
   - Define o delimitador como ponto-e-vírgula (`;`).

2. **Mapeamento das Colunas (`row[index]`)**:
   - As posições do array `row` correspondem às colunas do arquivo CSV, começando em `0`.

3. **Conversões Específicas**:
   - `toInteger(row[3])`: Converte a coluna **Matriz/Filial** para um número inteiro.
   - `date(row[6])`: Converte a data da situação cadastral para o formato de data do Neo4j.
   - `split(row[12], ',')`: Divide a lista de CNAEs Secundárias em um array.

4. **Campos Opcionais**:
   - Valores ausentes, como em `complemento`, `fax`, ou `telefone2`, serão salvos como `null`.

---

### **Validação dos Dados**
Após executar o comando, você pode verificar se os dados foram carregados corretamente:

- **Exibir os primeiros nós:**
   ```cypher
   MATCH (e:Estabelecimento)
   RETURN e.cnpj_base, e.nome_fantasia, e.cnae_fiscal_principal
   LIMIT 10;
   ```

- **Contar os nós criados:**
   ```cypher
   MATCH (e:Estabelecimento)
   RETURN COUNT(e) AS total_estabelecimentos;
   ```

---

## Linha de comando (cypher-shell)
```sh
docker exec -it \
neo4j-lab-container cypher-shell -u neo4j -p SuperSenha123 \
"LOAD CSV FROM 'file:///estabelecimentos.csv' AS row FIELDTERMINATOR ';' CREATE (:Estabelecimento { cnpj_base: row[0], cnpj_ordem: row[1], cnpj_dv: row[2], matriz_filial: toInteger(row[3]), nome_fantasia: row[4], situacao_cadastral: row[5], data_situacao_cadastral: date(row[6]), motivo_situacao_cadastral: row[7], cidade_exterior: row[8], codigo_pais: row[9], data_inicio_atividade: date(row[10]), cnae_fiscal_principal: row[11], cnaes_secundarias: split(row[12], ','), tipo_logradouro: row[13], logradouro: row[14], numero: row[15], complemento: row[16], bairro: row[17], cep: row[18], uf: row[19], codigo_municipio: row[20], ddd_telefone1: row[21], telefone1: row[22], ddd_telefone2: row[23], telefone2: row[24], ddd_fax: row[25], fax: row[26], email: row[27], situacao_especial: row[28], data_situacao_especial: row[29] });"

```

---

# DESCRIBE TABLE

No **Neo4j**, não existe um comando direto equivalente ao `DESCRIBE TABLE` dos bancos relacionais, mas você pode obter informações sobre as **propriedades associadas a uma label** usando consultas específicas ou chamadas do sistema. Aqui está como proceder para a label `Estabelecimento`:

---

### **1. Usar `CALL db.schema.nodeTypeProperties()`**
Este comando retorna todas as propriedades associadas às labels no banco de dados, incluindo `Estabelecimento`. 

#### **Comando:**
```cypher
CALL db.schema.nodeTypeProperties()
YIELD nodeLabels, propertyName, propertyTypes
WHERE "Estabelecimento" IN nodeLabels
RETURN propertyName, propertyTypes;
```

#### **O que este comando faz:**
- Lista as propriedades associadas à label `Estabelecimento`.
- Mostra o nome e o tipo de cada propriedade.

---

### **2. Inspecionar um Nó com a Label**
Se quiser visualizar diretamente as propriedades de um nó específico da label `Estabelecimento`, use uma consulta como esta:

#### **Comando:**
```cypher
MATCH (e:Estabelecimento)
RETURN keys(e) AS propriedades
LIMIT 1;
```

#### **O que este comando faz:**
- Retorna todas as propriedades presentes em um nó da label `Estabelecimento`.

---

### **3. Listar Todas as Labels no Banco**
Se você quer verificar a existência da label `Estabelecimento`:

#### **Comando:**
```cypher
CALL db.labels();
```

---

### **Usando na Linha de Comando (CLI)**
Para executar qualquer um dos comandos acima via `cypher-shell`, use a seguinte sintaxe no terminal:

```bash
docker exec -it neo4j-lab-container cypher-shell -u neo4j -p SuperSenha123 "CALL db.schema.nodeTypeProperties() YIELD nodeLabels, propertyName, propertyTypes WHERE 'Estabelecimento' IN nodeLabels RETURN propertyName, propertyTypes;"
```

---

### **Exemplo de Saída Esperada**
Se os nós de `Estabelecimento` têm as propriedades carregadas corretamente, o comando deve retornar algo como:

| **propertyName**      | **propertyTypes** |
|------------------------|-------------------|
| `cnpj_base`           | `STRING`          |
| `nome_fantasia`       | `STRING`          |
| `situacao_cadastral`  | `STRING`          |
| `data_inicio_atividade`| `DATE`           |


---

# Sócios

Com base no sample do arquivo `socios.csv` e no layout correspondente do PDF, aqui está o comando de carga para a **Label `Socio`** no Neo4j:

---

### **Comando de Carga para a Label `Socio`**

```cypher
LOAD CSV FROM 'file:///socios.csv' AS row
FIELDTERMINATOR ';'
CREATE (:Socio {
  cnpj_base: row[0],
  identificador_socio: toInteger(row[1]),
  nome_socio: row[2],
  cpf_cnpj_socio: row[3],
  codigo_qualificacao_socio: row[4],
  data_entrada_sociedade: date(row[5]),
  codigo_pais: row[6],
  cpf_representante: row[7],
  nome_representante: row[8],
  codigo_qualificacao_representante: row[9],
  faixa_etaria: toInteger(row[10])
});
```

---

### **Explicação dos Campos**
1. **`cnpj_base`** (row[0]):
   - Identifica a empresa à qual o sócio está vinculado (8 primeiros dígitos do CNPJ).
   
2. **`identificador_socio`** (row[1]):
   - Identifica o tipo do sócio:
     - `1`: Pessoa Jurídica
     - `2`: Pessoa Física
     - `3`: Estrangeiro.
   
3. **`nome_socio`** (row[2]):
   - Nome do sócio.

4. **`cpf_cnpj_socio`** (row[3]):
   - CPF (ou CNPJ para pessoa jurídica) do sócio.

5. **`codigo_qualificacao_socio`** (row[4]):
   - Código que identifica a qualificação do sócio (ex.: administrador, diretor, etc.).

6. **`data_entrada_sociedade`** (row[5]):
   - Data de entrada do sócio na empresa (convertida para o formato de data do Neo4j).

7. **`codigo_pais`** (row[6]):
   - Código do país (para sócios estrangeiros).

8. **`cpf_representante`** (row[7]):
   - CPF do representante legal (se aplicável).

9. **`nome_representante`** (row[8]):
   - Nome do representante legal (se aplicável).

10. **`codigo_qualificacao_representante`** (row[9]):
    - Código de qualificação do representante legal.

11. **`faixa_etaria`** (row[10]):
    - Faixa etária do sócio:
      - `1`: Menor de 18 anos
      - `2`: Entre 18 e 25 anos
      - `3`: Entre 26 e 30 anos
      - etc.

---

### **Considerações Especiais**
1. **Formato de Data:**
   - `date(row[5])` converte a string de data (formato `AAAA-MM-DD`) para o tipo `DATE` do Neo4j.

2. **Campos Numéricos:**
   - Campos como `identificador_socio`, `codigo_qualificacao_socio`, e `faixa_etaria` são convertidos para inteiros com `toInteger()`.

3. **Campos Nulos:**
   - Campos ausentes (ex.: `""`) serão automaticamente armazenados como `null` no Neo4j.

---

### **Testar a Carga**
Após carregar os dados, verifique se os nós foram criados corretamente:

- **Exibir um subconjunto de nós:**
   ```cypher
   MATCH (s:Socio)
   RETURN s.nome_socio, s.cpf_cnpj_socio, s.cnpj_base
   LIMIT 10;
   ```

- **Contar o total de nós criados:**
   ```cypher
   MATCH (s:Socio)
   RETURN COUNT(s) AS total_socios;
   ```

---

### **Carregar Usando o Terminal no Docker**
Se estiver utilizando o Neo4j via Docker Compose, o comando para carregar o arquivo via linha de comando seria:

```bash
docker exec -it neo4j-lab-container cypher-shell -u neo4j -p SuperSenha123 "LOAD CSV FROM 'file:///socios.csv' AS row FIELDTERMINATOR ';' CREATE (:Socio { cnpj_base: row[0], identificador_socio: toInteger(row[1]), nome_socio: row[2], cpf_cnpj_socio: row[3], codigo_qualificacao_socio: row[4], data_entrada_sociedade: date(row[5]), codigo_pais: row[6], cpf_representante: row[7], nome_representante: row[8], codigo_qualificacao_representante: row[9], faixa_etaria: toInteger(row[10]) });"
```

Para determinar o **layout** do arquivo `socios.csv` e elaborar o comando de carga, eu me baseei em:

---

### **1. O Sample do Arquivo `socios.csv`**
O sample fornecido tem dados delimitados por ponto-e-vírgula (`;`) e segue um padrão consistente para cada registro. Cada linha contém 11 campos:

```plaintext
"34152447";"2";"ANTONIO PAULO NETO";"***749831**";"49";"19990713";"";"***000000**";"";"00";"7"
```

Pela análise, cada campo parece corresponder a informações de um sócio e sua relação com uma empresa.

---

### **2. O Layout Disponível no PDF (Arquivo `LAYOUT_DADOS_ABERTOS_CNPJ.pdf`)**
No PDF enviado, a seção específica para sócios aparece em **"LAYOUT SOCIOS"**, detalhando os campos de cada registro. Aqui está o mapeamento que utilizei:

| **Campo do Sample**        | **Descrição no Layout**                           | **Posição no Arquivo** | **Observação**                                    |
|----------------------------|---------------------------------------------------|-------------------------|--------------------------------------------------|
| `"34152447"`               | **CNPJ Base**                                    | 1                       | Número base do CNPJ (8 primeiros dígitos).      |
| `"2"`                      | **Identificador de Sócio**                       | 2                       | `1`: Pessoa Jurídica, `2`: Pessoa Física, etc.  |
| `"ANTONIO PAULO NETO"`     | **Nome do Sócio ou Razão Social**                | 3                       | Nome do sócio (ou razão social para PJ).        |
| `"***749831**"`            | **CPF/CNPJ do Sócio**                            | 4                       | CPF ou CNPJ do sócio (mascarado no sample).     |
| `"49"`                     | **Código de Qualificação do Sócio**              | 5                       | Ex.: administrador, diretor, etc.              |
| `"19990713"`               | **Data de Entrada na Sociedade**                 | 6                       | Data no formato `AAAAMMDD`.                     |
| `""`                       | **Código do País**                               | 7                       | Código do país (para sócios estrangeiros).      |
| `"***000000**"`            | **CPF do Representante Legal**                   | 8                       | CPF do representante legal (mascarado).        |
| `""`                       | **Nome do Representante Legal**                  | 9                       | Nome do representante legal.                   |
| `"00"`                     | **Código de Qualificação do Representante Legal**| 10                      | Ex.: procurador, gestor, etc.                  |
| `"7"`                      | **Faixa Etária**                                 | 11                      | `1`: Menor de 18 anos, `2`: 18-25 anos, etc.   |

---

### **3. Regras de Transformação e Detalhes**
Com base no layout e na análise dos dados:
- **Identificação de Tipos de Dados**:
  - `CNPJ Base`, `CPF/CNPJ do Sócio`, e `CPF Representante` são strings.
  - Datas (`Data de Entrada na Sociedade`) são convertidas para o tipo `DATE` no Neo4j.
  - Números como `Identificador de Sócio` e `Código de Qualificação` são convertidos para inteiros.

- **Valores Ausentes**:
  - Campos vazios (`""`) são tratados como `null` no Neo4j.

- **Campos Especiais**:
  - A faixa etária (`7`) segue a codificação fornecida no layout, indicando grupos de idade.

---

### **Por que esse Layout?**
O layout descrito no PDF e a consistência dos dados no sample permitiram associar cada campo com seu significado correspondente. O comando foi elaborado com base nessas observações para garantir a carga correta no banco.
