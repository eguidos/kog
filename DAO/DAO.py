from pyspark.sql import SparkSession


class Spark:
    def __init__(self):
        self.spark = SparkSession.builder.appName('KOG').getOrCreate()

    @property
    def initialize(self):
        return self.spark

