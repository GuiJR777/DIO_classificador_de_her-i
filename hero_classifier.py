MIN_LEVEL = 0
MAX_LEVEL = 1
CLASS_NAME = 2
LAST_CLASS_LEVEL = -1


class HeroClassifier:
    def __init__(self, level) -> None:
        self.__level = int(level)

        self.__levels = [
            [0, 1000, "Ferro"],
            [1001, 2000, "Bronze"],
            [2001, 5000, "Prata"],
            [5001, 7000, "Ouro"],
            [7001, 8000, "Platina"],
            [8001, 9000, "Ascendente"],
            [9001, 10000, "Imortal"],
            [10001, "_", "Radiante"],
        ]

    def classify(self) -> str:
        if self.__level >= self.__levels[LAST_CLASS_LEVEL][MIN_LEVEL]:
            return self.__levels[LAST_CLASS_LEVEL][CLASS_NAME]

        for class_level in self.__levels:
            if (
                self.__level >= class_level[MIN_LEVEL] and
                self.__level <= class_level[MAX_LEVEL]
            ):
                return class_level[CLASS_NAME]
