# Projeto de Deploy de Machine Learning

## Descrição do problema

Este projeto tem como objetivo disponibilizar um modelo de Machine Learning por meio de uma API HTTP.

O modelo é treinado utilizando um dataset público e posteriormente salvo em um arquivo `.pkl`. A API desenvolvida em Python carrega esse modelo e recebe novos dados por meio de requisições HTTP, retornando a previsão realizada em formato JSON.

---

## Dataset utilizado

**Dataset:** `TODO`

**Fonte:** `TODO — Kaggle / UCI Machine Learning Repository`

**Link:** `TODO`

---

## Variável que está sendo prevista

**Variável alvo:** `TODO`

O modelo utiliza as características fornecidas na entrada para prever o valor da variável alvo definida durante o treinamento.

---

## Instruções para execução local

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd NOME_DO_REPOSITORIO
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

No Windows, ative o ambiente:

```bash
.venv\Scripts\activate
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

## Exemplo de requisição e resposta da API

### Requisição

```http
POST /predict
Content-Type: application/json
```

```json
[
  {
    "feature_1": 10.5,
    "feature_2": 3.2,
    "feature_3": 7.8
  }
]
```

> O exemplo será atualizado com os atributos reais do dataset utilizado.

### Resposta

```json
{
  "predicao": [
    "resultado"
  ]
}
```
