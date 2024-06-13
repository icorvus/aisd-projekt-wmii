import random

class Porter:
    def __init__(self, number, hands_position):
        self.number = number
        self.hands_position = hands_position

class Relacje:
    def __init__(self, num_porters):
        self.porters = self.create_porters(num_porters)
        self.relations = self.create_relations()

    def create_porters(self, num_porters):
        porters = []
        for i in range(1, num_porters + 1):
            hands_position = input(f"Podaj pozycję rąk tragarza {i} (przód/tył): ")
            porters.append(Porter(i, hands_position))
        return porters

    def create_relations(self):
        possible_pairs = [(porter1.number, porter2.number) for porter1 in self.porters for porter2 in self.porters if porter1 != porter2]
        relations = {}
        while possible_pairs:
            pair = random.choice(possible_pairs)
            if pair not in relations.keys() and (pair[1], pair[0]) not in relations.keys() and (pair[0], pair[1]) not in relations.keys():
                relation = random.choice([0, 1])  # 0 - Nie lubią się, 1 - Lubią się
                relations[pair] = relation
                possible_pairs.remove(pair)
                possible_pairs.remove((pair[1], pair[0]))
        return relations

    def display_relations(self):
        for pair, relation in self.relations.items():
            print(f"Tragarz {pair[0]} i tragarz {pair[1]}: {relation}")