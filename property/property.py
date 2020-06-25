from pyspark.sql.types import StructField, IntegerType, StringType, StructType


class Aluno(StructType):
    @property
    def aluno(self):
        return StructType([
            StructField('ID_EXECUCAO', IntegerType(), False),
            StructField('CDALUN',StringType(), False),
            StructField('NOME_ALUNO', StringType(), False),
            StructField('NOT_USED_COLUMN', StringType(), False),
            StructField('DECISAO', StringType(), False),
            StructField('COD1', StringType(), False)
        ])