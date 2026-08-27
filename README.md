# Projeto de Deploy de Machine Learning

## Integrantes

| RM | Nome |
|---|---|
| RM561408 | Gustavo Crevelari Monteiro Porto |
| RM561996 | Lucca de Araujo Gomes |
| RM561671 | Rafaela Ferreira Santos |
| RM566224 | Victor Sabelli Rocha Batista |

## Descrição do problema

Este projeto implementa uma API para disponibilizar um modelo de classificação de qualidade de vinhos. A tarefa de negócio
é transformar medições físico-químicas (por exemplo, acidez, teor alcoólico, sulfatos, densidade etc.) em uma predição
simples sobre a qualidade do produto: o modelo produz um rótulo binário `quality_label` indicando se o vinho é
considerado de qualidade 'boa' (1) ou 'não tão boa' (0).

O objetivo é demonstrar um fluxo completo de deploy: treinar um modelo com um dataset público, salvar o artefato em disco
(arquivo `.pkl`/`.joblib`) e expô‑lo por meio de uma API REST feita em Python/Flask. A API recebe um JSON com as características
do vinho, aplica o pré‑processamento mínimo necessário e retorna a predição em JSON.

---

## Dataset utilizado

**Dataset:** Wine Quality

**Fonte:** Kaggle / UCI Machine Learning Repository

**Link:** https://www.kaggle.com/datasets/rajyellow46/wine-quality?resource=download


## Notebook utilizado

**Notebook:** deploy_ml\CP4_IoT.ipynb

## Variável que está sendo prevista

**Variável alvo:** `quality_label` — rótulo binário de qualidade do vinho

O modelo utiliza as características fornecidas na entrada para prever uma versão binária da coluna `quality` do dataset original.
Foi criada a coluna `quality_label` onde `1` indica vinho de qualidade considerada boa (nota >= 6) e
`0` indica vinho de qualidade considerada não tão boa (nota <= 5).

---

## Instruções para execução local

Clone o repositório:

```bash
git clone https://github.com/GusCrevelari/CP4-Deploy-ML-Flask
```

Entre na pasta do projeto:

```bash
cd CP4-Deploy-ML-Flask
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
python inference.py
```

A aplicação ficará disponível localmente em:

```text
http://localhost:8000
```

---

## Instruções para testar a API

A API pode ser testada localmente utilizando o **Postman**.

Utilize:

```text
Método: POST
URL: http://localhost:8000/predict
Content-Type: application/json
```

No Postman:

1. selecione o método `POST`;
2. informe a URL `http://localhost:8000/predict`;
3. acesse `Body`;
4. selecione `raw`;
5. selecione o formato `JSON`;
6. envie os dados esperados pelo modelo;
7. clique em `Send`.

A API retornará a previsão em formato JSON.

---

### JSON de exemplo para Postman

Cole o JSON abaixo em **Body → raw → JSON** no Postman e clique em `Send`.

```json
[
  {
    "type": "white",
    "fixed acidity": 7.2,
    "volatile acidity": 0.24,
    "citric acid": 0.30,
    "residual sugar": 1.6,
    "chlorides": 0.048,
    "free sulfur dioxide": 27.0,
    "total sulfur dioxide": 131.0,
    "density": 0.9933,
    "pH": 3.25,
    "sulphates": 0.45,
    "alcohol": 10.5
  }
]
```


## Exemplos de requisições (PowerShell e curl)

Antes de testar, inicie a API a partir da pasta `deploy_ml`:

```powershell
cd D:\cp4\deploy_ml\CP4-Deploy-ML-Flask\deploy_ml
python .\inference.py
```

A seguir há cinco exemplos em uma linha para chamar `POST /predict`.

- Exemplo 1 — amostra única (vinho tinto) em PowerShell:
  ```powershell
  Invoke-RestMethod -Uri 'http://127.0.0.1:8000/predict' -Method Post -ContentType 'application/json' -Body '{"fixed acidity":7.4,"volatile acidity":0.7,"citric acid":0,"residual sugar":1.9,"chlorides":0.076,"free sulfur dioxide":11,"total sulfur dioxide":34,"density":0.9978,"pH":3.51,"sulphates":0.56,"alcohol":9.4,"type":"red"}'
  ```

- Exemplo 2 — amostra única (vinho branco) em PowerShell:
  ```powershell
  Invoke-RestMethod -Uri 'http://127.0.0.1:8000/predict' -Method Post -ContentType 'application/json' -Body '{"fixed acidity":6.8,"volatile acidity":0.30,"citric acid":0.34,"residual sugar":2.5,"chlorides":0.045,"free sulfur dioxide":15,"total sulfur dioxide":54,"density":0.9937,"pH":3.20,"sulphates":0.65,"alcohol":11.0,"type":"white"}'
  ```

- Exemplo 3 — duas amostras (array) em PowerShell:
  ```powershell
  Invoke-RestMethod -Uri 'http://127.0.0.1:8000/predict' -Method Post -ContentType 'application/json' -Body '[{"fixed acidity":7.4,"volatile acidity":0.7,"citric acid":0,"residual sugar":1.9,"chlorides":0.076,"free sulfur dioxide":11,"total sulfur dioxide":34,"density":0.9978,"pH":3.51,"sulphates":0.56,"alcohol":9.4,"type":"red"},{"fixed acidity":6.8,"volatile acidity":0.30,"citric acid":0.34,"residual sugar":2.5,"chlorides":0.045,"free sulfur dioxide":15,"total sulfur dioxide":54,"density":0.9937,"pH":3.20,"sulphates":0.65,"alcohol":11.0,"type":"white"}]'
  ```

- Exemplo 4 — ler JSON de arquivo e enviar (PowerShell):
  ```powershell
  '{"fixed acidity":7.4,"volatile acidity":0.7,"citric acid":0,"residual sugar":1.9,"chlorides":0.076,"free sulfur dioxide":11,"total sulfur dioxide":34,"density":0.9978,"pH":3.51,"sulphates":0.56,"alcohol":9.4,"type":"red"}' > .\sample.json
  Invoke-RestMethod -Uri 'http://127.0.0.1:8000/predict' -Method Post -ContentType 'application/json' -InFile .\sample.json
  ```

- Exemplo 5 — usar `curl.exe` no Windows (escapar aspas):
  ```powershell
  curl.exe -s -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"fixed acidity\":7.4,\"volatile acidity\":0.7,\"citric acid\":0,\"residual sugar\":1.9,\"chlorides\":0.076,\"free sulfur dioxide\":11,\"total sulfur dioxide\":34,\"density\":0.9978,\"pH\":3.51,\"sulphates\":0.56,\"alcohol\":9.4,\"type\":\"red\"}"
  ```

Se preferir, copie os exemplos para o Postman ou outra ferramenta de API. A resposta da API é JSON com a chave `prediction` e, quando disponível, `probabilities`.
