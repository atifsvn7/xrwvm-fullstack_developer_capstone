from .models import CarMake, CarModel


def initiate():

    # Delete existing data first so we don't create duplicates
    CarModel.objects.all().delete()
    CarMake.objects.all().delete()

    # Create Car Makes
    car_makes = [
        {
            "name": "NISSAN",
            "description": "Nissan Motor Co., Ltd."
        },
        {
            "name": "Mercedes",
            "description": "Mercedes-Benz automobile manufacturer."
        },
        {
            "name": "Audi",
            "description": "German automobile manufacturer."
        },
        {
            "name": "Kia",
            "description": "South Korean automobile manufacturer."
        },
        {
            "name": "Toyota",
            "description": "Japanese automobile manufacturer."
        }
    ]

    makes = {}

    for make in car_makes:
        car_make = CarMake.objects.create(
            name=make["name"],
            description=make["description"]
        )
        makes[make["name"]] = car_make

    # Create Car Models
    car_models = [
        ("NISSAN", "Altima", "SEDAN", 2023),
        ("NISSAN", "Rogue", "SUV", 2023),
        ("NISSAN", "Versa", "SEDAN", 2023),

        ("Mercedes", "C-Class", "SEDAN", 2023),
        ("Mercedes", "GLC", "SUV", 2023),
        ("Mercedes", "E-Class", "SEDAN", 2023),

        ("Audi", "A4", "SEDAN", 2023),
        ("Audi", "Q5", "SUV", 2023),
        ("Audi", "A6", "SEDAN", 2023),

        ("Kia", "Sorento", "SUV", 2023),
        ("Kia", "Sportage", "SUV", 2023),
        ("Kia", "Rio", "SEDAN", 2023),

        ("Toyota", "Camry", "SEDAN", 2023),
        ("Toyota", "RAV4", "SUV", 2023),
        ("Toyota", "Corolla", "SEDAN", 2023),
    ]

    for make, name, car_type, year in car_models:
        CarModel.objects.create(
            car_make=makes[make],
            name=name,
            type=car_type,
            year=year
        )

    print("Car makes and car models populated successfully.")