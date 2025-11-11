from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.getOrCreate()

spark.sql("show catalogs").show()
