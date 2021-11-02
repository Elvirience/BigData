class Worker:

    def __init__(self, name, surname, position, income={"wage": 1000000, "bonus": 1000000}):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    """
    Достаю приватные оклад и бонус
    """
    def get_wage(self):
        return self.__income.get("wage")

    def get_bonus(self):
        return self.__income.get("bonus")


class Position(Worker):

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        return self.get_wage() + self.get_bonus()


worker = Position("Egor", "Ageev", "Teamlead")
worker.get_full_name()
print(worker.get_total_income())
