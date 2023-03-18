import datetime
from time import time

from django.db import models

types = [('Staff','Staff'),('Visitor','Visitor')]
doctors = [('0','Not Alloted'),('1','Cardiology- Dr. Ajit R Menon'),('2','Cardiology- Dr. Amit M Vora'),('3','Cardiology- Dr. Robin Pinto'),('4','Dermatology- Dr. Dipali Malvankar'),('5','Dermatology-  Dr. Jisha Pillai'),('6','Dentisty- Dr. Jigar Gala'),('7','Gastroenterology-Dr. Samir S Parikh'),('8','Gastroenterology-Dr. Mehul Choksi'),('9','Dibetology and Endocrinology-Dr Vijay K Panikar'),('10','Dibetology and Endocrinology-Dr Shashank R Joshi'),('11','Gynaecology- Dr. Swarna Goyal'),('12','Gynaecology- Dr.  Cherry C Shah'),('13','IVF-Dr. Rishma Dhillon Pai'),('14','Neurology- Dr. Girishkumar Soni'),('15','Neurology- Dr. Ajay C Vyas'),('16','Oncology-Dr. Archana Swami'),('17','Paediatrics- Dr.Deepak Ugra'),('18','Pathology- Dr. Asha M George'),('19','Urology-Dr. BK Dastur'),('20','Urology-Dr. Rupin Shah')]

class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    ranking = models.CharField(max_length=20)
    profession = models.CharField(max_length=200)
    status = models.CharField(choices=types,max_length=20,null=True,blank=False,default='Visitor')
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    shift = models.TimeField()
    age=models.IntegerField()

    bg=models.CharField(max_length=10)
    ephone=models.BigIntegerField()
    address=models.CharField(max_length=100)
    aadhar=models.BigIntegerField()
    languages=models.CharField(max_length=100)
    physician=models.CharField(max_length=100)
    allergies=models.CharField(max_length=100)
    height=models.CharField(max_length=50)
    weight=models.CharField(max_length=50)
    condition=models.CharField(max_length=100)
    drugs=models.CharField(max_length=100)
    marital_status=models.CharField(max_length=100)

    doctor = models.CharField(choices=doctors,max_length=20,null=True,blank=False,default='0')


    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face
