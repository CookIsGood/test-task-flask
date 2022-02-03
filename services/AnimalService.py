from repositories.AnimalRepository import AnimalRepository
from model.AnimalModel import AnimalOut, AnimalIn
from typing import List
animalRepo = AnimalRepository()


class AnimalService:

    def search_by_name(self, name: str) -> List[AnimalOut]:
        result = []
        for item in animalRepo.search_by_name(name):
            result.append(AnimalOut.parse_obj(item))
        return result

    def create(self, name, type_animal, speed, predator):
        animal = {
            'name': name,
            'type': type_animal,
            'speed': speed,
            'predator': predator
        }
        return animalRepo.create(AnimalIn.parse_obj(animal))
