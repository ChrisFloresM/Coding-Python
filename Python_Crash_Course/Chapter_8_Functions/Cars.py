#Christian Flores 12/02/2021

def make_car(manufacturer, model, **car):
    car["manufacturer"] = manufacturer
    car["model"] = model
    return car

my_first_car = make_car("Chevrolet", "Spark", color = "blue", tow_package = True)
print(my_first_car)
