import random
from bicycles import Bicycle, BikeShop, Customer

# Create a list of Bikes, then create a BikeShop, stock it
# with Bikes...

bikes = [
    Bicycle("Desert Cruiser", 35, 1500), Bicycle("Rock Climber", 25, 3800),
    Bicycle("Speed Racer", 15, 10000), Bicycle("The Aspen", 20, 8500),
    Bicycle("City Ride", 40, 855), Bicycle("Low Rider", 50, 5550)
    ]

shop = BikeShop("Bill's Bikes", 20, bikes)

# Create a list of Customers, then iterate over them, print
# the Customer's name and Bikes they can afford to buy...

customers = [Customer("Joe", 6000), Customer("Tom", 8000), Customer("Jim", 15000)]

for customer in customers:

    bikes = ", ".join( bike.model for bike in shop.filter(customer.fund) )
    print (customer.name, "|", bikes)

# Print BikeShop before making sales...

print (shop)

# Iterate over the customers, sell each a Bike, then list customer,
# what they bought, the cost, and how much $ they have left...

template = "{0} bought the {1} at ${2}, and they have ${3} left over."

for customer in customers:
    
    affordables = shop.filter(customer.fund)
    shop.sell(random.choice(affordables), customer)
    
    print (template.format(
        customer.name, customer.bike.model,
        customer.bike.price, customer.fund
        ))

# Print BikeShop after making sales...

print (shop)
