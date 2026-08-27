# Projeto de Deploy de Machine Learning

## Descrição do problema

Este projeto tem como objetivo disponibilizar um modelo de Machine Learning por meio de uma API HTTP.

O modelo é treinado utilizando um dataset público e posteriormente salvo em um arquivo `.pkl`. A API desenvolvida em Python carrega esse modelo e recebe novos dados por meio de requisições HTTP, retornando a previsão realizada em formato JSON.

---

## Dataset utilizado

**Dataset:** Wine Quality

**Fonte:** Kaggle / UCI Machine Learning Repository

**Link:** https://www.kaggle.com/datasets/rajyellow46/wine-quality?resource=download

---

## Variável que está sendo prevista

**Variável alvo:** `TODO`

O modelo utiliza as características fornecidas na entrada para prever o valor da variável alvo definida durante o treinamento.

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
