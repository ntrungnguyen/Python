class Animal:
    def __init__(self, name: str, age: int, sex: str) -> None:
        self._name = name
        self._age = age
        self._sex = sex
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
        
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, name):
        self._age = name
        
        
    @property
    def sex(self):
        return self._sex
    @sex.setter
    def sex(self, name):
        self._sex = name
        
    def voice(self):
        pass
    
    def __str__(self) -> str:
        return f"{self._name}\t{self.age}\t{self.sex}"
    
    def __repr__(self) -> str:
        return f"{self._name}\t{self.age}\t{self.sex}"

        
        
class Dog(Animal):
    def __init__(self, name: str, age: int, sex: str) -> None:
        super().__init__(name, age, sex)
        
    def __str__(self) -> str:
        return super().__str__() + f"{self.voice()}"
    
    def voice(self):
        return "Gâu gâu gâu"
    
class Frog(Animal):
    
    def __init__(self, name: str, age: int, sex: str) -> None:
        super().__init__(name, age, sex)
        
    def __str__(self) -> str:
        return super().__str__() + f"{self.voice()}"
    
    def voice(self):
        print( "Ếch ộp ếch ộp")
    
    

class Cat(Animal):
    def __init__(self, name: str, age: int, sex: str) -> None:
        super().__init__(name, age, sex)
        
    def __str__(self) -> str:
        return super().__str__() + f"{self.voice()}"
    
    def voice(self):
        return "Mèo méo meo"
    
class kitten(Cat):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, sex = "Cái")
        
    def __str__(self) -> str:
        return super().__str__() #+ f"{self.sex}"
    
class Tomcat(Cat):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, sex = "Đực")
        
    def __str__(self) -> str:
        return super().__str__() + f"{self.sex}"
    

bun = Dog('Bun', 15, 'Đực')
foggy = Frog('Froggy', 10, 'Đực')
kittie = kitten('Kittie', 17)
linh = kitten('Linh', 15)
tom = Tomcat('Tom', 20)
jerry = Tomcat('Jerry', 15)

listAnimals = []
listAnimals.append(bun)
listAnimals.append(foggy)
listAnimals.append(linh)
listAnimals.append(jerry)
listAnimals.append(kittie)
listAnimals.append(tom)

print(listAnimals.__str__())