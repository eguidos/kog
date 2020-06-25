import random
from DAO.DAO import Spark
from property.property import Aluno

class Dataframe:
    def __init__(self, path):
        self.spark = Spark().initialize
        self.path = path
        self.schema = Aluno().aluno
        self.df = self.start

    @property
    def start(self):
        return self.spark.read.load(self.path, format="csv", header="true", sep=",", schema=self.schema)


class Execution:
    @property
    def get_id(self):
        return [random.randrange(1, 10000, 1) for _ in range(10)]

