from abc import ABCMeta, abstractmethod


class AbstSearch:
    __metaclass__ = ABCMeta

    @abstractmethod
    def search_in_data(self, data, condition):
        pass


class AnimalSearch(AbstSearch):

    def search_in_data(self, data, condition):
        result = []
        for count, value in enumerate(data):
            if value['name'] == condition:
                result.append(data[count])
        return result
