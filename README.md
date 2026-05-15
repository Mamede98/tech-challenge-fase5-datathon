# 🔮 Sistema de Alerta Educacional - Passos Mágicos

## 📌 Sobre o Projeto
Este projeto foi desenvolvido como solução para o Datathon da **Associação Passos Mágicos** como requisito do challenge fase5. O objetivo principal é utilizar Ciência de Dados e Machine Learning para prever e identificar precocemente alunos em risco de defasagem escolar, fornecendo à equipe pedagógica uma ferramenta de apoio à decisão para intervenções rápidas e direcionadas.

## 🎯 O Desafio e a Solução Preditiva
A defasagem escolar é um problema multifatorial. Para enfrentá-lo, desenvolvemos um modelo de classificação utilizando o algoritmo **Random Forest Classifier**.

**Nosso principal *insight* analítico:** Ao treinar o modelo focado nos indicadores acadêmicos e psicopedagógicos (IDA, IEG, IPP, IPV) junto à Fase do aluno, alcançamos um **Recall de ~75%** na identificação de alunos em risco. No entanto, a acurácia geral estabilizou na casa dos 66%-67%. 

Longe de ser uma falha, essa métrica fornece um diagnóstico para o negócio: **notas e indicadores de engajamento sozinhos não são suficientes para explicar 100% da realidade do aluno**. Isso valida analiticamente a necessidade da ONG de manter um olhar humanizado e aponta para o próximo passo de maturidade de dados: a integração de variáveis socioeconômicas (como estrutura familiar e rede de ensino).

## 📁 Estrutura do Repositório
Para garantir a reprodutibilidade, o projeto está estruturado da seguinte forma:

- 📂 `data/`: Contém os arquivos CSV com as bases de dados históricas e tratadas.
- 📂 `notebooks/`: Arquivos `.ipynb` documentando todo o processo de limpeza, Análise Exploratória (EDA) e treinamento do modelo de Machine Learning.
- 📄 `app.py`: Código-fonte da interface visual interativa.
- 📄 `modelo_passos_magicos.pkl`: Modelo preditivo treinado e empacotado para deploy.
- 📄 `requirements.txt`: Lista de bibliotecas e dependências necessárias para rodar a aplicação.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Manipulação de Dados:** Pandas e NumPy
- **Machine Learning:** Scikit-Learn
- **Deploy e Frontend:** Streamlit

## 🚀 Como Acessar e Executar

### 🌐 Acesso em Nuvem (Recomendado)
A aplicação foi implementada no Streamlit Community Cloud e pode ser testada diretamente pelo navegador:
👉 **[https://tech-challenge-fase5-datathon-mgrx3yanwhvunpwqerkj5v.streamlit.app/]**

### 💻 Execução Local
Caso deseje rodar o projeto em sua própria máquina, siga os passos abaixo:

1. Clone este repositório.
2. Abra o terminal na pasta raiz do projeto.
3. Instale as dependências executando:
```bash
pip install -r requirements.txt