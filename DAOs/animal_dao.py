from DAOs.dao import DAO
from entidades.animal import Animal

class AnimalDAO(DAO):
    def __init__(self):
        super().__init__('animais.pkl')
        
    def add(self, animal: Animal):
        if isinstance(animal, Animal):
            super().add(animal.codigo, animal)

    def update(self, animal: Animal):
        if isinstance(animal, Animal):
            super().update(animal.codigo, animal)

    def remove(self, key: int):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)
