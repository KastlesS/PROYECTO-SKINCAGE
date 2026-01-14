from faker import Faker
from .models import Usuario
import random 

fake = Faker("es_ES")

def crearUser(n):
    for i in range(n):
        Usuario.objects.create(nombre=fake.name(),email=fake.email(), id_usuario=fake.unique.random_number(digits=4), balance=fake.pydecimal(positive=True, left_digits=4, right_digits=2), tel=fake.phone_number())
