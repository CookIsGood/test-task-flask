from entity.AnimalEntity import Animal
from buisness_logic import AnimalSearch
from conn_db import db
from model.AnimalModel import AnimalIn


class AnimalRepository(Animal):

    def get_all(self):
        animals = self.query.all()
        content = []
        for count, value in enumerate(animals):
            animal = {
                'id': value.id,
                'name': value.name,
                'type': value.type,
                'speed': value.speed,
                'predator': value.predator,
            }
            content.append(animal)
        return content

    def search_by_name(self, name):
        result_search = AnimalSearch().search_in_data(data=self.get_all(), condition=name)
        return result_search

    def create(self, animal_in: AnimalIn):
        animal = Animal(name=animal_in.name, type=animal_in.type, speed=animal_in.speed,
                        predator=animal_in.predator)
        db.session.add(animal)
        db.session.commit()
        return animal

