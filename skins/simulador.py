from faker import Faker
from .models import Skin
import random 

fake = Faker("es_ES")

def crearSkin(n):
    for i in range(n):
        Skin.objects.create(nombre=fake.name(),stattrack=fake.boolean(), id_skin=fake.unique.random_number(digits=4), desgaste=fake.pydecimal(positive=True, left_digits=1, right_digits=12), precio=fake.pydecimal(positive=True, left_digits=4, right_digits=2),stock = fake.random_number(digits=3))
