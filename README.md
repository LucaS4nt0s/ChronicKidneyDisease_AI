# 🩺 ChronicKidneyDisease_AI - Predição de Doença Renal Crônica com Machine Learning

![Python](https://img.shields.io/badge/Language-Python%203-blue.svg)
![Machine Learning](https://img.shields.io/badge/Field-Machine%20Learning%20%7C%20AI-orange.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-F7931E.svg)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626.svg)

## 📌 Visão Geral
Este projeto realiza um estudo aprofundado de **Ciência de Dados e Aprendizado de Máquina**, aplicando técnicas rigorosas de pré-processamento de dados e algoritmos de classificação supervisionada para a detecção precoce de **Doença Renal Crônica (CKD - Chronic Kidney Disease)**.

O diagnóstico preditivo utiliza uma base clínica contendo múltiplos exames laboratoriais e dados demográficos de pacientes, passando por tratamento de valores faltantes (imputação), categorização, normalização, balanceamento e validação de modelos com métricas de desempenho para contextos médicos.

---

## 🚀 Etapas da Metodologia de IA
1. 🔍 **Análise Exploratória e Classificação de Atributos**:
   - Identificação da variável-alvo (`class`: *ckd* vs *notckd*).
   - Análise de escala dos atributos (quantitativos contínuos/discretos e qualitativos nominais/ordinais).
   - Diagnóstico do desbalanceamento de classes na base de dados (400 amostras: 250 ckd e 150 notckd).
2. 🧹 **Pré-processamento e Engenharia de Features**:
   - Limpeza e tratamento de ruídos em strings e valores ambíguos.
   - Imputação de dados ausentes (estratégias baseadas em média/mediana para numéricos e moda para categóricos).
   - Codificação de atributos nominais e binários (One-Hot Encoding / Label Encoding).
   - Padronização e normalização de escala (Z-score / Min-Max Scaling).
3. 🤖 **Treinamento e Validação de Classificadores**:
   - Divisão estratificada em conjuntos de Treino e Teste (`train_test_split` / K-Fold Cross Validation).
   - Avaliação com modelos consagrados (Árvores de Decisão, Random Forest, SVM, KNN e Regressão Logística).
4. 📈 **Avaliação Crítica de Resultados**:
   - Cálculo de Acurácia, Precisão, Recall (Sensibilidade), F1-Score e Matriz de Confusão.
   - Enfoque em minimizar falsos negativos (erro crítico em triagens clínicas).

---

## 🛠️ Tecnologias e Ferramentas
- **Linguagem**: Python 3.10+
- **Bibliotecas de Manipulação e ML**:
  - `Pandas` e `NumPy` para manipulação estruturada de matrizes e DataFrames
  - `Scikit-Learn` para pipeline de pré-processamento, imputação e algoritmos preditivos
  - `Matplotlib` e `Seaborn` para visualizações gráficas de dispersão, correlação e matrizes de confusão
- **Formato da Base**: Arquivos ARFF (`.arff`) e tabulares processados em ambiente Jupyter Notebook.

---

## 📂 Estrutura do Repositório
```plaintext
ChronicKidneyDisease_AI/
└── src/
    ├── relatorio_analise.ipynb             # Notebook completo com pipeline, código executado e interpretação
    ├── ExecVenv.md                         # Guia de configuração e ativação do ambiente virtual Python
    └── base_de_dados/
        ├── chronic_kidney_disease.arff     # Conjunto de dados primário em formato ARFF
        ├── chronic_kidney_disease_full.arff# Versão consolidada dos registros médicos
        └── chronic_kidney_disease.info.txt # Dicionário de dados e metadados dos atributos clínicos
```

---

## ⚙️ Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.8 ou superior instalado.
- Gerenciador de pacotes `pip`.

### Configuração do Ambiente Virtual
1. Clone o repositório:
   ```bash
   git clone https://github.com/LucaS4nt0s/ChronicKidneyDisease_AI.git
   cd ChronicKidneyDisease_AI/src
   ```
2. Crie e ative o ambiente virtual (`venv`):
   - **No Windows (cmd/PowerShell):**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **No Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. Instale as dependências:
   ```bash
   pip install notebook scikit-learn pandas numpy matplotlib seaborn scipy
   ```
4. Inicialize o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
5. Abra e execute as células do arquivo `relatorio_analise.ipynb`.

---

## 👨‍💻 Autor
Desenvolvido por **Luca Samuel dos Santos** ([@LucaS4nt0s](https://github.com/LucaS4nt0s)).
