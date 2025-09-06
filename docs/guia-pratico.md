
# 📘 Guia Prático: Versionamento de Notebooks com Azure Databricks

## 1. Criar Cluster
- No portal Azure, acesse o **Databricks Workspace**.
- Crie um cluster com runtime suportado por PySpark.

## 2. Importar Notebooks
- Vá em **Workspace > Import**.
- Faça upload dos notebooks `.ipynb` ou conecte com **Azure DevOps Repos**.

## 3. Executar Notebooks
- Abra e rode os notebooks `exemplo_filtros` e `exemplo_visualizacoes`.
- Valide as saídas (tabelas, gráficos).

## 4. Versionamento com DevOps
- Conecte o Databricks ao **Azure Repos**.
- Habilite sincronização automática de notebooks.

## 5. CI/CD
- Use o arquivo `azure-pipelines.yml` para automatizar testes de notebooks.
- Configure triggers para rodar a cada `push`.

---
✅ Resultado esperado:
- Notebooks organizados e versionados.
- Execução validada via DevOps.
- Ambiente colaborativo, seguro e reprodutível.
