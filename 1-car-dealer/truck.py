from vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.carry_limit = None
        self.current_carriage_weight = None

    def has_carriage(self):
        return bool(current_carriage_weight)

    def attach_carriage(self, weight):
        pass
