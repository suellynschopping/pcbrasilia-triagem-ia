Aula 2 – IA & Machine Learning Aplicado à Segurança Pública 
IBMEC  

Exercicio Streamlit 

 

Guia Prático – Construindo uma Aplicação Web de Triagem Inteligente com Machine Learning + Mini‑RAG usando Streamlit e GitHub 

Objetivo da Aula 

Nesta atividade prática, os alunos irão construir, versionar e publicar uma aplicação web de Inteligência Artificial para triagem de ocorrências da Polícia Civil de Brasília, utilizando Machine Learning, uma base de conhecimento (Mini‑RAG), GitHub e Streamlit Cloud. 

Arquitetura da Solução 

Usuário → Streamlit Web App → Modelo de Machine Learning → Mini‑RAG (Base de Conhecimento) → Resposta Inteligente 
 
GitHub armazena o código | Streamlit executa o app na nuvem 

1. Criando o Repositório no GitHub 

1. Acesse https://github.com 
2. Clique em New Repository 
3. Nome: pcbrasilia-triagem-ia 
4. Marque Public 
5. Clique em Create repository 

2. Estrutura do Projeto 

Crie os arquivos no repositório: 
- app.py  → código principal do Streamlit 
- requirements.txt → dependências do projeto 
- README.md → explicação do projeto 

3. Conteúdo do requirements.txt 

streamlit 
pandas 
numpy 
scikit-learn 
