#coding=utf-8
from pyspark.sql import functions as f
from model.model import Dataframe
import os


class Transform:

    def __init__(self, id_execution):
        self.id_execution = id_execution
        self.df = Dataframe(os.path.join(os.path.dirname(__file__), '../aluno.csv')).start
        self.df = self.change_columns(self.df)
        self.df = self.drop_columns(self.df)
        self.select_columns(self.df)
        self.write_aws('peanut/kog')

    @property
    def get_df(self):
        return self.df

    def change_columns(self, df):
        df = df.withColumn("ID_EXECUCAO", f.lit(self.id_execution))
        df = df.withColumn("CODIGO_ALUNO", f.col("CDALUN"))

        # caso COD1 não seja igual a "A", a coluna "DECISAO" deve ser False
        df = df.withColumn("DECISAO", f.when(f.lit(df["COD1"]) == 'A', f.lit(True)).
                           otherwise(f.lit(False)))
        return df

    def drop_columns(self, df):
        df = df.drop("NOT_USED_COLUMN")
        df = df.drop("CODIGO_ALUNO")
        return df

    def select_columns(self, df):
        print(df.select("*").show(truncate=False))

    def write_aws(self, path):
        self.df.write.parquet("s3a://"+path+"")
        pass
