class Controller:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing {self.name} controller")