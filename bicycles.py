class Customer:

    def __init__(self, name, fund):

        self.name = name
        self.fund = fund
        self.bike = None

class Bicycle:

    def __init__(self, model, weight, cost):

        self.model = model
        self.weight = weight
        self.cost = cost

    def __repr__(self):

        template = "The {0} | Cost: ${1}, Weight: {2}lbs"
        return template.format(self.model, self.cost, self.weight)

class BikeShop:

    def __init__(self, name, margin, bikes):

        self.name = name
        self.margin = margin

        self.profit = 0
        self.inventory = {}

        for bike in bikes:

            bike.markup = int((bike.cost / 100.0) * self.margin)
            bike.price = bike.cost + bike.markup
            self.inventory[bike.model] = bike

    def __repr__(self):

        template = "\n{0} (${1} profit)\n{2}\n"
        bikes = "\n".join( str(bike) for bike in self.inventory.values() )
        return template.format(self.name, self.profit, bikes)

    def filter(self, budget):

        bikes = self.inventory.values()
        return [ bike for bike in bikes if bike.price <= budget ]

    def sell(self, bike, customer):

        customer.bike = bike
        customer.fund -= bike.price
        self.profit += bike.markup
        del self.inventory[bike.model]
        