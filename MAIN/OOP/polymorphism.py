

class Employe:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

    def work(self):
        print(f"{self.name} work...")

class SoftwareEnginner(Employe):
    def __init__(self,name,age,city,level): #override attribute
        super().__init__(name,age,city)
        self.level=level
    def coding(self):
        print(f"{self.name} is coding...")

    def work(self):
        print(f"{self.name} minning...") #override method

class Desiger(Employe):
    def drawing(self):
        print(f"{self.name} is drawing...")

    def work(self):
        print(f"{self.name} edtiing...") #override method

employees=[SoftwareEnginner('lal',44,'ragam','junior'),
          SoftwareEnginner('kal',3,'gdf','senior'),
          SoftwareEnginner('lfdf',43,'ragam','jff'),
          Desiger('chill',34,"gdfds")
          ]
def motiation():
    for employ in employees:
        employ.work()
        print(employ.name)

motiation()