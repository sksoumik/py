def information(**data):
    for key, value in data.items():
        print(f"{key}: {value}")


information(Firstname="Sadman", Lastname="Soumik", Age=26, Phone=1234567890)
information(
    Firstname="John",
    Lastname="Wood",
    Email="johnwood@nomail.com",
    Country="Wakanda",
    Age=25,
    Phone=9876543210,
)
