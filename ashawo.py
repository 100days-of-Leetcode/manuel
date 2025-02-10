class Ashawo:
    def __init__(self, name, age, isActive, streak):
        self.name = name
        self.age = age
        self.streak = streak
        self.isActive = isActive

    def current_status(self):
        print(f"The status of {self.name} is {self.isActive}")

    def show_streak(self):
        if self.streak <= 1:
            print("Good")
        elif self.streak == 2:
            print("hmm")
        else:
            print("Too much chale")

class Pro(Ashawo):
    def __init__(self, name, age, isActive, streak, stats):
        super().__init__(self.name, self.age, self.isActive,self.streak)
        self.stats = stats

    def get_current_status(self):
        return self.stats

    def set_current_status(self, status):
        if status == "Active":
            print("In the game")
        else:
            print("Retired")


kay = Ashawo("Kaydee",21, True, 3
             )
drew = Ashawo("Drew", 21, True, 5)
drew.current_status()
drew.show_streak()

safo = Ashawo("Safo", 21, True, 7)
safo.current_status()
safo.show_streak()

odk = Ashawo("Odk", 22, True, 4)
odk.current_status()
odk.show_streak()

nana = Ashawo("Nana", 20, False, 0)
nana.current_status()
nana.show_streak()
