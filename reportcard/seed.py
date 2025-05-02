import os 
import django 
import random 
from faker import Faker 
from reportcard.models import Student
os.environ.setdefault('DJANGO_SETTINGS_MODULE','reportcard_project.settings')
django.setup()
fake=Faker()
def create_fake_students(n=50):
    for _ in range(n):
        s1=random.randint(40,100)
        s2=random.randint(40,100)
        s3=random.randint(30,100)
        Student.objects.create(
            name=fake.name(),
            email=fake.email(),
            age=random.randint(10,18),
            address=fake.address(),
            subject1=s1,subject2=s2,subject3=s3
        )
    print(f'{n} fake student records generated successfully')

if __name__=='__main__':
    create_fake_students()