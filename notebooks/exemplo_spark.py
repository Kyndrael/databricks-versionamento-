
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Criar sessão Spark
spark = SparkSession.builder.appName("ExemploSpark").getOrCreate()

# Dados de exemplo
dados = [(1, "Jonathan", 28, "SP"),
         (2, "Maria", 34, "RJ"),
         (3, "José", 21, "SP"),
         (4, "Ana", 30, "MG")]

df = spark.createDataFrame(dados, ["id", "nome", "idade", "estado"])

# Mostrar dados iniciais
print("📌 Dados iniciais:")
df.show()

# Filtrar apenas SP
df_sp = df.filter(col("estado") == "SP")

print("📌 Pessoas de SP:")
df_sp.show()

# Média de idade
df.groupBy("estado").agg(avg("idade").alias("idade_media")).show()
