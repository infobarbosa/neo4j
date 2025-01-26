# Relacionamentos
```cypher
CALL db.relationshipTypes()
```

```cypher
MATCH (n)-[r]->(m)
RETURN labels(n) AS StartLabels, type(r) AS RelationshipType, labels(m) AS EndLabels, COUNT(*) AS RelationshipCount
ORDER BY RelationshipCount DESC;
```

```
[
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Estabelecimento"
      ],
      "LOCALIZADO_EM",
      [
        "Municipio"
      ],
      {
        "low": 63723860,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Empresa"
      ],
      "POSSUI",
      [
        "Estabelecimento"
      ],
      {
        "low": 63723860,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Socio"
      ],
      "SOCIO_DE",
      [
        "Empresa"
      ],
      {
        "low": 25077167,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Empresa"
      ],
      "TEM_COMO_SOCIO",
      [
        "Socio"
      ],
      {
        "low": 25077167,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Estabelecimento"
      ],
      "CLASSIFICADO_COMO",
      [],
      {
        "low": 14668000,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Estabelecimento"
      ],
      "LOCALIZADO_EM",
      [],
      {
        "low": 14668000,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Estabelecimento"
      ],
      "CLASSIFICADO_COMO",
      [
        "Natureza"
      ],
      {
        "low": 3771,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  }
]
```


# WEG: 
```cypher
CNPJ: 84.429.695/0001-11
CNPJ base: 84429695
```

# Vale
```cypher
O CNPJ da Vale S.A. é 33.592.510/0001-54
CNPJ base: 33592510
```

# WEG

### WEG SA [Empresa]
```cypher
MATCH (e:Empresa {cnpj_base: "84429695"})
RETURN e
```

```json
{
  "identity": 27200085,
  "labels": [
    "Empresa"
  ],
  "properties": {
    "natureza_juridica": "2046",
    "situacao_cadastral": "05",
    "cnpj_base": "84429695",
    "capital_social": 7504516508.0,
    "razao_social": "WEG SA",
    "porte": "10"
  },
  "elementId": "27200085"
}
```

### WEG SA [Estabelecimento]
```cypher
MATCH (e:Estabelecimento)
WHERE e.cnpj_base= "84429695"
AND e.identificador_matriz_filial = "1"
RETURN e
```

```json
{
  "identity": 162469010,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "AVENIDA",
    "ddd_fax": "47",
    "numero": "3300",
    "situacao_cadastral": "02",
    "identificador_matriz_filial": "1",
    "data_situacao_cadastral": "20051103",
    "cep": "89256900",
    "uf": "SC",
    "cnae_fiscal_principal": "6462000",
    "complemento": "",
    "natureza_juridica": "47",
    "ddd_telefone_2": "32764000",
    "cnpj_base": "84429695",
    "ddd_telefone_1": "47",
    "motivo_situacao_cadastral": "00",
    "email": "32764775",
    "municipio": "8175",
    "bairro": "VILA LALAU",
    "pais": "",
    "cnae_fiscal_secundaria": "2071100,2610800,2651500,2710401,2710402,2710403,2732500,3313901,3314701,3314799,4663000,4669999,4673700,4742300,7020400,7112000,7490199",
    "data_inicio_atividade": "19690529",
    "cnpj_dv": "11",
    "logradouro": "PREFEITO WALDEMAR GRUBBA",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0001",
    "nome_fantasia": "WEG"
  },
  "elementId": "162469010"
}
```

### WEG SA [Socio]
```cypher
MATCH (s:Socio)
WHERE s.cpf_cnpj_socio = "84429695000111"
RETURN s
```

```json
{
  "identity": 5903964,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20221223",
    "tipo": "1",
    "nome_representante": "***569108**",
    "cnpj_base": "10953379",
    "qualificacao_representante": "ANDRE LUIS RODRIGUES",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "5903964"
}
{
  "identity": 10312935,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20190226",
    "tipo": "1",
    "nome_representante": "***366129**",
    "cnpj_base": "05729768",
    "qualificacao_representante": "WILSON JOSE WATZKO",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "10312935"
}
{
  "identity": 10935212,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20100705",
    "tipo": "1",
    "nome_representante": "***104659**",
    "cnpj_base": "01422798",
    "qualificacao_representante": "SERGIO LUIZ SILVA SCHWARTZ",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "10935212"
}
{
  "identity": 12920398,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20130206",
    "tipo": "1",
    "nome_representante": "***366129**",
    "cnpj_base": "11299346",
    "qualificacao_representante": "WILSON JOSE WATZKO",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "12920398"
}
{
  "identity": 17599938,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20150320",
    "tipo": "1",
    "nome_representante": "***000000**",
    "cnpj_base": "06056296",
    "qualificacao_representante": "",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "00",
    "cpf_representante": ""
  },
  "elementId": "17599938"
}
{
  "identity": 24228054,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20100622",
    "tipo": "1",
    "nome_representante": "***104659**",
    "cnpj_base": "96570148",
    "qualificacao_representante": "SERGIO LUIZ SILVA SCHWARTZ",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "24228054"
}
{
  "identity": 25024662,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "19801209",
    "tipo": "1",
    "nome_representante": "***466179**",
    "cnpj_base": "75397463",
    "qualificacao_representante": "ALIDOR LUEDERS",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "25024662"
}
{
  "identity": 27259773,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20100527",
    "tipo": "1",
    "nome_representante": "***366129**",
    "cnpj_base": "12006058",
    "qualificacao_representante": "WILSON JOSE WATZKO",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "27259773"
}
{
  "identity": 27400396,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20230125",
    "tipo": "1",
    "nome_representante": "***569108**",
    "cnpj_base": "13434970",
    "qualificacao_representante": "ANDRE LUIS RODRIGUES",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "27400396"
}
{
  "identity": 33662263,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20071004",
    "tipo": "1",
    "nome_representante": "***466179**",
    "cnpj_base": "09109119",
    "qualificacao_representante": "ALIDOR LUEDERS",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "33662263"
}
{
  "identity": 34341950,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20110603",
    "tipo": "1",
    "nome_representante": "***569108**",
    "cnpj_base": "13772125",
    "qualificacao_representante": "ANDRE LUIS RODRIGUES",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "34341950"
}
{
  "identity": 39983043,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20241114",
    "tipo": "1",
    "nome_representante": "***569108**",
    "cnpj_base": "60621141",
    "qualificacao_representante": "ANDRE LUIS RODRIGUES",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "39983043"
}
{
  "identity": 41104307,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20110914",
    "tipo": "1",
    "nome_representante": "***569108**",
    "cnpj_base": "14309992",
    "qualificacao_representante": "ANDRE LUIS RODRIGUES",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "41104307"
}
{
  "identity": 47184656,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "21",
    "data_entrada": "20021114",
    "tipo": "1",
    "nome_representante": "***000000**",
    "cnpj_base": "08520438",
    "qualificacao_representante": "",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "00",
    "cpf_representante": ""
  },
  "elementId": "47184656"
}
{
  "identity": 52062446,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20110112",
    "tipo": "1",
    "nome_representante": "***000000**",
    "cnpj_base": "00668382",
    "qualificacao_representante": "",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "00",
    "cpf_representante": ""
  },
  "elementId": "52062446"
}
{
  "identity": 60659363,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "20190515",
    "tipo": "1",
    "nome_representante": "***366129**",
    "cnpj_base": "02810190",
    "qualificacao_representante": "WILSON JOSE WATZKO",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "05",
    "cpf_representante": ""
  },
  "elementId": "60659363"
}
{
  "identity": 67415096,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "84429695000111",
    "qualificacao": "22",
    "data_entrada": "19990601",
    "tipo": "1",
    "nome_representante": "***000000**",
    "cnpj_base": "83150714",
    "qualificacao_representante": "",
    "nome": "WEG SA",
    "codigo_pais": "0",
    "faixa_etaria": "00",
    "cpf_representante": ""
  },
  "elementId": "67415096"
}
```

### WEG EQUIPAMENTOS E LOGISTICA LTDA [Empresa]

```cypher
match(e:Empresa) WHERE e.cnpj_base = "10953379" 
RETURN e
```

```json
{
  "identity": 45716230,
  "labels": [
    "Empresa"
  ],
  "properties": {
    "natureza_juridica": "2062",
    "situacao_cadastral": "05",
    "cnpj_base": "10953379",
    "capital_social": 366000000.0,
    "razao_social": "WEG EQUIPAMENTOS E LOGISTICA LTDA",
    "porte": "05"
  },
  "elementId": "45716230"
}
```

### WEG EQUIPAMENTOS E LOGISTICA LTDA [Estabelecimento]
```cypher
MATCH (e:Estabelecimento {cnpj_base: "10953379"})
RETURN e
```

Output:
```json
{
  "identity": 96909916,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "RUA",
    "ddd_fax": "",
    "numero": "100",
    "situacao_cadastral": "02",
    "identificador_matriz_filial": "1",
    "data_situacao_cadastral": "20090630",
    "cep": "88311720",
    "uf": "SC",
    "cnae_fiscal_principal": "2710402",
    "complemento": "BLOCO 15",
    "natureza_juridica": "47",
    "ddd_telefone_2": "32764000",
    "cnpj_base": "10953379",
    "ddd_telefone_1": "47",
    "motivo_situacao_cadastral": "00",
    "email": "",
    "municipio": "8161",
    "bairro": "CORDEIROS",
    "pais": "",
    "cnae_fiscal_secundaria": "2731700,3313901,3321000,4619200,4669999,4673700,4693100,5250801,5250802,6462000,7112000,7120100,7490199,8299799",
    "data_inicio_atividade": "20090630",
    "cnpj_dv": "08",
    "logradouro": "ROSA ORSI DALCOQUIO",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0001",
    "nome_fantasia": "***"
  },
  "elementId": "96909916"
}
{
  "identity": 171072473,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "AVENIDA",
    "ddd_fax": "47",
    "numero": "3300",
    "situacao_cadastral": "02",
    "identificador_matriz_filial": "2",
    "data_situacao_cadastral": "20090630",
    "cep": "89256900",
    "uf": "SC",
    "cnae_fiscal_principal": "4693100",
    "complemento": "      PISO SUPERIOR",
    "natureza_juridica": "47",
    "ddd_telefone_2": "32764000",
    "cnpj_base": "10953379",
    "ddd_telefone_1": "47",
    "motivo_situacao_cadastral": "00",
    "email": "32764775",
    "bairro": "VILA LALAU",
    "municipio": "8175",
    "cnae_fiscal_secundaria": "8299799",
    "pais": "",
    "data_inicio_atividade": "20090630",
    "cnpj_dv": "99",
    "logradouro": "PREFEITO WALDEMAR GRUBBA",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0002",
    "nome_fantasia": "WEG LOGISTICA"
  },
  "elementId": "171072473"
}
```

```cypher
MATCH (e:Empresa {cnpj_base: "84429695"})<-[:SOCIO_DE]-(s:Socio)
RETURN e, collect(s) AS socios
```



```cypher
MATCH (e:Empresa )<-[:SOCIO_DE]-(s:Socio)
WHERE e.cnpj_base = "84429695"
RETURN e, collect(s) AS socios
```


# CNPJ              : 83.489.963/0001-28 [ MATRIZ ]
# Nome da empresa	: WPA PARTICIPACOES E SERVICOS S.A.
```cypher
Match(s:Socio {cpf_cnpj_socio: "83489963000128"}) return s
```

```cypher
MATCH (s:Socio)
WHERE s.cpf_cnpj_socio = "83489963000128" AND s.cnpj_base = "84429695"
RETURN s;
```

# weg
```cypher
MATCH (s:Socio)
WHERE s.cpf_cnpj_socio = "84429695000111"
RETURN s;
```

```cypher
MATCH (weg:Socio {cpf_cnpj_socio: "84429695000111"})-[:SOCIO_DE]->(empresa:Empresa)<-[:SOCIO_DE]-(outro_socio:Socio)
RETURN weg AS socio_weg, empresa, collect(outro_socio) AS outros_socios;
```


```cypher
MATCH (weg:Socio )-[:SOCIO_DE]->(empresa:Empresa)
WHERE weg.cpf_cnpj_socio= "84429695000111"
RETURN weg AS socio_weg, collect(empresa) AS empresas;
```

Desenvolva uma consulta que, a partir da empresa Weg (cnpj base 84429695), obtenha as empresas onde a Weg é sócia.
Veja, eu não estou buscando os sócios da Weg e sim as empresas onde a Weg tem sociedade.
A partir daí também quero os demais sócios das empresas obtidas.
Ficaria assim:
- nível 1: Weg (o nó principal)
- nível 2: As empresas onde a Weg é sócia
- nível 3: os sócios das empresas obtidas no nível 2

```
MATCH (weg:Empresa {cnpj_base: "84429695"})<-[:SOCIO_DE]-(wegSocio:Socio)-[:SOCIO_DE]->(empresaNivel2:Empresa)
WITH weg, empresaNivel2
OPTIONAL MATCH (empresaNivel2)<-[:SOCIO_DE]-(outroSocio:Socio)
RETURN weg AS empresa_nivel1, 
       collect(DISTINCT empresaNivel2) AS empresas_nivel2, 
       collect(DISTINCT outroSocio) AS socios_nivel3;

```

# Prompt

Escreva uma consulta que retorne o seguinte:
- Nível 1 [Label Empresa] recebe como entrada um cnpj base e retorna os dados dessa empresa
Exemplo do Label Empresa:
```json
  {
    "identity": 27200085,
    "labels": [
      "Empresa"
    ],
    "properties": {
      "natureza_juridica": "2046",
      "situacao_cadastral": "05",
      "cnpj_base": "84429695",
      "capital_social": 7504516508.0,
      "razao_social": "WEG SA",
      "porte": "10"
    },
    "elementId": "27200085"
  }
```

- Nível 2 [Label Estabelecimento] recebe como entrada o cnpj base da empresa do nível 1 e retorna os estabelecimentos dessa empresa
Método de relacionamento: Empresa.cnpj_base = Estabelecimento.cnpj_base
Exemplo do label Estabelecimento:
```json
{
  "identity": 112549171,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "AVENIDA",
    "ddd_fax": "",
    "numero": "4243",
    "situacao_cadastral": "08",
    "identificador_matriz_filial": "2",
    "data_situacao_cadastral": "19890727",
    "cep": "54420010",
    "uf": "PE",
    "cnae_fiscal_principal": "8888888",
    "complemento": "SALA 10",
    "natureza_juridica": "",
    "ddd_telefone_2": "",
    "cnpj_base": "84429695",
    "ddd_telefone_1": "",
    "motivo_situacao_cadastral": "01",
    "email": "",
    "municipio": "2457",
    "bairro": "PIEDADE",
    "cnae_fiscal_secundaria": "",
    "pais": "",
    "data_inicio_atividade": "19870720",
    "cnpj_dv": "79",
    "logradouro": "BERNARDO VIEIRA DE MELO",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0009",
    "nome_fantasia": "NORWEG"
  },
  "elementId": "112549171"
}
{
  "identity": 130396560,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "RUA",
    "ddd_fax": "",
    "numero": "3000",
    "situacao_cadastral": "08",
    "identificador_matriz_filial": "2",
    "data_situacao_cadastral": "20110304",
    "cep": "89260160",
    "uf": "SC",
    "cnae_fiscal_principal": "8299799",
    "complemento": "",
    "natureza_juridica": "",
    "ddd_telefone_2": "",
    "cnpj_base": "84429695",
    "ddd_telefone_1": "",
    "motivo_situacao_cadastral": "01",
    "email": "",
    "municipio": "8175",
    "bairro": "CENTRO",
    "pais": "",
    "cnae_fiscal_secundaria": "6399200,7410299,7490105,7490199,8219999,8299703,8299707",
    "data_inicio_atividade": "19731008",
    "cnpj_dv": "45",
    "logradouro": "JOINVILLE",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0005",
    "nome_fantasia": "WEG"
  },
  "elementId": "130396560"
}
{
  "identity": 130396561,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "RUA",
    "ddd_fax": "",
    "numero": "399",
    "situacao_cadastral": "08",
    "identificador_matriz_filial": "2",
    "data_situacao_cadastral": "20110304",
    "cep": "89252230",
    "uf": "SC",
    "cnae_fiscal_principal": "8299799",
    "complemento": "",
    "natureza_juridica": "",
    "ddd_telefone_2": "",
    "cnpj_base": "84429695",
    "ddd_telefone_1": "",
    "motivo_situacao_cadastral": "01",
    "email": "",
    "municipio": "8175",
    "bairro": "CENTRO",
    "pais": "",
    "cnae_fiscal_secundaria": "6399200,7410299,7490105,7490199,8219999,8299703,8299707",
    "data_inicio_atividade": "19840524",
    "cnpj_dv": "07",
    "logradouro": "VENANCIO DA SILVA PORTO",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0007",
    "nome_fantasia": "WEG"
  },
  "elementId": "130396561"
}
{
  "identity": 143141329,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "AVENIDA",
    "ddd_fax": "",
    "numero": "862",
    "situacao_cadastral": "08",
    "identificador_matriz_filial": "2",
    "data_situacao_cadastral": "20110407",
    "cep": "04077000",
    "uf": "SP",
    "cnae_fiscal_principal": "7490104",
    "complemento": "",
    "natureza_juridica": "",
    "ddd_telefone_2": "",
    "cnpj_base": "84429695",
    "ddd_telefone_1": "",
    "motivo_situacao_cadastral": "01",
    "email": "",
    "municipio": "7107",
    "bairro": "INDIANOPOLIS",
    "pais": "",
    "cnae_fiscal_secundaria": "",
    "data_inicio_atividade": "19700916",
    "cnpj_dv": "00",
    "logradouro": "MOEMA",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0002",
    "nome_fantasia": "WEG"
  },
  "elementId": "143141329"
}
{
  "identity": 149513715,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "AVENIDA",
    "ddd_fax": "",
    "numero": "474",
    "situacao_cadastral": "08",
    "identificador_matriz_filial": "2",
    "data_situacao_cadastral": "19930423",
    "cep": "91220580",
    "uf": "RS",
    "cnae_fiscal_principal": "8888888",
    "complemento": "1 ANDAR",
    "natureza_juridica": "",
    "ddd_telefone_2": "",
    "cnpj_base": "84429695",
    "ddd_telefone_1": "",
    "motivo_situacao_cadastral": "01",
    "email": "",
    "municipio": "8801",
    "bairro": "SAO JOAO",
    "pais": "",
    "cnae_fiscal_secundaria": "",
    "data_inicio_atividade": "19781205",
    "cnpj_dv": "98",
    "logradouro": "PARA",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0008",
    "nome_fantasia": "WEG"
  },
  "elementId": "149513715"
}
{
  "identity": 155731546,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "RUA",
    "ddd_fax": "",
    "numero": "S N",
    "situacao_cadastral": "08",
    "identificador_matriz_filial": "2",
    "data_situacao_cadastral": "19930423",
    "cep": "89260160",
    "uf": "SC",
    "cnae_fiscal_principal": "0210101",
    "complemento": "",
    "natureza_juridica": "",
    "ddd_telefone_2": "",
    "cnpj_base": "84429695",
    "ddd_telefone_1": "",
    "motivo_situacao_cadastral": "01",
    "email": "",
    "municipio": "8175",
    "bairro": "",
    "pais": "",
    "cnae_fiscal_secundaria": "",
    "data_inicio_atividade": "19731008",
    "cnpj_dv": "26",
    "logradouro": "JOINVILE",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0006",
    "nome_fantasia": "WEG"
  },
  "elementId": "155731546"
}
{
  "identity": 161924249,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "RUA",
    "ddd_fax": "",
    "numero": "30",
    "situacao_cadastral": "08",
    "identificador_matriz_filial": "2",
    "data_situacao_cadastral": "19960315",
    "cep": "20911000",
    "uf": "RJ",
    "cnae_fiscal_principal": "7490101",
    "complemento": "",
    "natureza_juridica": "",
    "ddd_telefone_2": "",
    "cnpj_base": "84429695",
    "ddd_telefone_1": "",
    "motivo_situacao_cadastral": "01",
    "email": "",
    "municipio": "6001",
    "bairro": "BENFICA",
    "pais": "",
    "cnae_fiscal_secundaria": "",
    "data_inicio_atividade": "19700225",
    "cnpj_dv": "83",
    "logradouro": "ITAPOAN",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0003",
    "nome_fantasia": "WEG"
  },
  "elementId": "161924249"
}
{
  "identity": 162469010,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "AVENIDA",
    "ddd_fax": "47",
    "numero": "3300",
    "situacao_cadastral": "02",
    "identificador_matriz_filial": "1",
    "data_situacao_cadastral": "20051103",
    "cep": "89256900",
    "uf": "SC",
    "cnae_fiscal_principal": "6462000",
    "complemento": "",
    "natureza_juridica": "47",
    "ddd_telefone_2": "32764000",
    "cnpj_base": "84429695",
    "ddd_telefone_1": "47",
    "motivo_situacao_cadastral": "00",
    "email": "32764775",
    "municipio": "8175",
    "bairro": "VILA LALAU",
    "pais": "",
    "cnae_fiscal_secundaria": "2071100,2610800,2651500,2710401,2710402,2710403,2732500,3313901,3314701,3314799,4663000,4669999,4673700,4742300,7020400,7112000,7490199",
    "data_inicio_atividade": "19690529",
    "cnpj_dv": "11",
    "logradouro": "PREFEITO WALDEMAR GRUBBA",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0001",
    "nome_fantasia": "WEG"
  },
  "elementId": "162469010"
}
{
  "identity": 175793831,
  "labels": [
    "Estabelecimento"
  ],
  "properties": {
    "tipo_logradouro": "RUA",
    "ddd_fax": "",
    "numero": "10",
    "situacao_cadastral": "08",
    "identificador_matriz_filial": "2",
    "data_situacao_cadastral": "19930423",
    "cep": "30430010",
    "uf": "MG",
    "cnae_fiscal_principal": "8888888",
    "complemento": "2 ANDAR SALA 21",
    "natureza_juridica": "",
    "ddd_telefone_2": "",
    "cnpj_base": "84429695",
    "ddd_telefone_1": "",
    "motivo_situacao_cadastral": "01",
    "email": "",
    "municipio": "4123",
    "bairro": "GUTIERREZ",
    "pais": "",
    "cnae_fiscal_secundaria": "",
    "data_inicio_atividade": "19810914",
    "cnpj_dv": "64",
    "logradouro": "ESTACIO DE SA",
    "nome_cidade_exterior": "",
    "cnpj_ordem": "0004",
    "nome_fantasia": "WEG"
  },
  "elementId": "175793831"
}
```

- Nível 3 as empresas onde os estabelecimentos do nível 2 são sócios
Método de relacionamento: 
  1. Estabelecimento[cnpj_base] = Empresa[cnpj_base] 
  2. Socio[cpf_cnpj_socio] = Estabelecimento[cnpj_base + cnpj_ordem + cnpj_dv]
  3. Empresa[cnpj_base] = Socio[cnpj_base]

Exemplo do label Socio:
```json
{
  "identity": 4091404,
  "labels": [
    "Socio"
  ],
  "properties": {
    "cpf_cnpj_socio": "***749831**",
    "qualificacao": "49",
    "data_entrada": "19990713",
    "tipo": "2",
    "nome_representante": "***000000**",
    "cnpj_base": "34152447",
    "qualificacao_representante": "",
    "nome": "ANTONIO PAULO NETO",
    "codigo_pais": "7",
    "faixa_etaria": "00",
    "cpf_representante": ""
  },
  "elementId": "4091404"
}
```

Observe a seguir como são os relacionamentos entre os Labels:
[
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Estabelecimento"
      ],
      "LOCALIZADO_EM",
      [
        "Municipio"
      ],
      {
        "low": 63723860,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Empresa"
      ],
      "POSSUI",
      [
        "Estabelecimento"
      ],
      {
        "low": 63723860,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Socio"
      ],
      "SOCIO_DE",
      [
        "Empresa"
      ],
      {
        "low": 25077167,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Empresa"
      ],
      "TEM_COMO_SOCIO",
      [
        "Socio"
      ],
      {
        "low": 25077167,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Estabelecimento"
      ],
      "CLASSIFICADO_COMO",
      [],
      {
        "low": 14668000,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Estabelecimento"
      ],
      "LOCALIZADO_EM",
      [],
      {
        "low": 14668000,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  },
  {
    "keys": [
      "StartLabels",
      "RelationshipType",
      "EndLabels",
      "RelationshipCount"
    ],
    "length": 4,
    "_fields": [
      [
        "Estabelecimento"
      ],
      "CLASSIFICADO_COMO",
      [
        "Natureza"
      ],
      {
        "low": 3771,
        "high": 0
      }
    ],
    "_fieldLookup": {
      "StartLabels": 0,
      "RelationshipType": 1,
      "EndLabels": 2,
      "RelationshipCount": 3
    }
  }
]


# Output
### Consulta sem relacionametno formal
```cypher
MATCH (empresa:Empresa {cnpj_base: "84429695"})-[:POSSUI]->(estabelecimento:Estabelecimento)
WITH empresa, estabelecimento
MATCH (socio:Socio)
WHERE socio.cpf_cnpj_socio = (estabelecimento.cnpj_base + estabelecimento.cnpj_ordem + estabelecimento.cnpj_dv)
RETURN 
  empresa AS Empresa, 
  estabelecimento AS Estabelecimento,
  socio AS Socio,
  "TEM_COMO_SOCIO" AS Relacionamento

```

### Consulta com relacionamento formal
##### Criação do relacionamento
```cypher
// Match nos estabelecimentos e sócios sem relação explícita
MATCH (estabelecimento:Estabelecimento), (socio:Socio)
WHERE socio.cpf_cnpj_socio = (estabelecimento.cnpj_base + estabelecimento.cnpj_ordem + estabelecimento.cnpj_dv)

// Criação do relacionamento TEM_COMO_SOCIO
MERGE (estabelecimento)-[:TEM_COMO_SOCIO]->(socio)
RETURN count(*) AS RelacionamentosCriados
```

##### A consulta
```cypher
// Nível 1: Recupera a empresa pelo cnpj_base
MATCH (empresa:Empresa {cnpj_base: "84429695"})

// Nível 2: Recupera os estabelecimentos associados à empresa
MATCH (empresa)-[:POSSUI]->(estabelecimento:Estabelecimento)

// Nível 3: Usa o relacionamento criado para conectar estabelecimentos aos sócios
MATCH (estabelecimento)-[:TEM_COMO_SOCIO]->(socio:Socio)

// Retorna os resultados
RETURN 
  empresa AS Empresa, 
  collect(DISTINCT estabelecimento) AS Estabelecimentos, 
  collect(DISTINCT socio) AS Socios
```
  