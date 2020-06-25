from business.transform import Transform
from model.model import Execution


class Main:
    def __init__(self):
        ids = Execution().get_id
        [Transform(id) for id in ids]


if __name__ == '__main__':
    Main()
