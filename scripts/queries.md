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

# Weg
```cypher
MATCH (e:Empresa {cnpj_base: "84429695"})
RETURN e
```

# Weg
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
