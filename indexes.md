# Índices

---


#### **Empresa**
```cypher
CREATE INDEX idx_empresa_cnpj_base IF NOT EXISTS FOR (e:Empresa) ON (e.cnpj_base);
```

#### **Estabelecimento**
```cypher
CREATE INDEX idx_estabelecimento_cnpj IF NOT EXISTS FOR (e:Estabelecimento) ON (e.cnpj_base, e.ordem, e.dv);
```

#### **Sócio**
```cypher
CREATE INDEX idx_socio_cnpj IF NOT EXISTS FOR (s:Socio) ON (s.cnpj_base, s.identificador_socio);
```

#### **Natureza Jurídica**
```cypher
CREATE INDEX idx_natureza_codigo IF NOT EXISTS FOR (n:Natureza) ON (n.codigo_natureza);
```

#### **Município**
```cypher
CREATE INDEX idx_municipio_codigo IF NOT EXISTS FOR (m:Municipio) ON (m.codigo_municipio);
```

#### **País**
```cypher
CREATE INDEX idx_pais_codigo IF NOT EXISTS FOR (p:Pais) ON (p.codigo_pais);
```

#### **Qualificação**
```cypher
CREATE INDEX idx_qualificacao_codigo IF NOT EXISTS FOR (q:Qualificacao) ON (q.codigo_qualificacao);
```

#### **Motivo**
```cypher
CREATE INDEX idx_motivo_codigo IF NOT EXISTS FOR (m:Motivo) ON (m.codigo_motivo);
```

