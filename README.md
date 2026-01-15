# 🧠 ChurnInsight — Modelo de Machine Learning

> Modelo de Machine Learning responsável por prever **churn de clientes**, utilizado como parte central do ecossistema **ChurnInsight**.

Este repositório contém todo o pipeline de **pré-processamento, treinamento, avaliação e serialização** do modelo de ML que é consumido pela API backend do projeto.

---

## 🚀 Visão Geral

O **ChurnInsight Model** é responsável por analisar dados de clientes e gerar uma **probabilidade de churn**, permitindo que sistemas de negócio tomem decisões baseadas em dados.

Ele faz parte de uma solução maior composta por:

| Componente      | Repositório                                                                                                      |
| --------------- | ---------------------------------------------------------------------------------------------------------------- |
| 🖥️ Frontend    | [https://github.com/isaacmnss/churnInsight-frontend](https://github.com/isaacmnss/churnInsight-frontend)         |
| ⚙️ API Backend  | [https://github.com/isaacmnss/churnInsight](https://github.com/isaacmnss/churnInsight) |
| 🧠 Modelo de ML | [https://github.com/isaacmnss/churnInsight-model](https://github.com/isaacmnss/churnInsight-model)               |

---

## 🎯 Objetivo do Modelo

O modelo tem como objetivo:

* Prever a chance de **evasão (churn)** de clientes
* Ajudar empresas a **antecipar perdas**
* Servir previsões para consumo via API REST

O output do modelo normalmente é:

* **Classe** (churn / não churn)
* **Probabilidade associada** à previsão

---

## 🧪 Dataset

O modelo foi treinado utilizando o **Bank Customer Churn Dataset**, disponível publicamente no Kaggle:

🔗 [https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn)

O dataset contém informações de clientes bancários com atributos demográficos, financeiros e comportamentais, como:

* Idade
* Score de crédito
* Saldo em conta
* Número de produtos
* Atividade do cliente

> ⚠️ O dataset é utilizado **exclusivamente para fins educacionais e de demonstração**. Os dados não representam clientes reais.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib / Seaborn** (análise exploratória)
* **Joblib / Pickle** (serialização do modelo)

---

## 🧩 Pipeline do Modelo

O fluxo geral do modelo segue as etapas abaixo:

1. **Carregamento dos dados**
2. **Limpeza e pré-processamento**

   * Tratamento de valores nulos
   * Encoding de variáveis categóricas
   * Normalização/Escala
3. **Treinamento do modelo**
4. **Avaliação (accuracy, precision, recall, etc.)**
5. **Serialização do modelo treinado**
6. **Integração com a API Backend**

---

## 🚀 Como Executar Localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/isaacmnss/churnInsight-model.git
cd churnInsight-model
```

### 2️⃣ Criar ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o treinamento

```bash
python train.py
```

> Indicativo: ajuste o nome do script conforme a estrutura real do projeto.

---

## 📦 Artefatos Gerados

Após o treinamento, são gerados arquivos como:

* 📁 Modelo treinado (`.pkl` ou `.joblib`)
* 📊 Métricas de avaliação
* 📈 Gráficos de desempenho

Esses artefatos são consumidos diretamente pela **API Backend**.

---

## 🔌 Integração com a API

A API Backend carrega o modelo treinado para:

* Receber dados de entrada via HTTP
* Executar a predição
* Retornar o resultado ao frontend

📌 Repositório da API:

```
https://github.com/isaacmnss/churnInsight
```

---

## 🧪 Testes e Avaliação

O modelo pode ser avaliado utilizando métricas como:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

Essas métricas ajudam a validar a qualidade das previsões.

---

## ❤️ Agradecimentos

Projeto desenvolvido no contexto de um **Hackathon** promovido por Alura e Oracle durante o bootcamp Oracle Next Education

Agradecimentos especiais ao restante dos membros da equipe:

### Data Scientists

- Pedro Camargo

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pedrocamargo1/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/Pdrnho)

- Suellen Costa


[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/suellensilva86)

- Antonio Sergio

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/asccjr/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/ASCCJR)

### Devs Backend

- Paulo Cruz

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/paulo-cruz-dev/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/PauloBrazilian)

- Isaaac Meneses

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/isaac-meneses/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/isaacmnss)
