from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone=models.CharField('telefon raqam',max_length=13)
    # rasm=models.ImageField()
    status_gender=(
        ('direktor','direktor'),
        ('yordamchi','yordamchi'),
        ('bo\'lim_rahbari','bo\'lim_rahbari' )
    )
    status=models.CharField(choices=status_gender,max_length=20,default='yordamchi')

class Bulim(models.Model):
    bolim_nomi=models.CharField(max_length=50)
    bolim_id=models.PositiveIntegerField()
    bolim_rahbari=models.OneToOneField(User,on_delete=models.CASCADE)

class Mahsulot(models.Model):
    mahsulot_id=models.PositiveIntegerField(unique=True)
    mahsulot_nomi=models.CharField(max_length=1000)

class Ishturi_or_Bolim(models.Model):
    name=models.CharField(max_length=100)
    ish_id=models.IntegerField(default=1,unique=True)

    def __str__(self):
        return '{} {}'.format(self.name,self.ish_id)

class Xodim(models.Model):
    class StatusChoices(models.TextChoices):
        gender_male='erkak','Erkak'
        gender_female='ayol','Ayol'
    status=models.CharField(choices=StatusChoices.choices,default=StatusChoices.gender_male,max_length=10)
    ism=models.CharField(max_length=50,error_messages={'required': 'this field is required'})
    familiya=models.CharField(max_length=50)                
    # rasm=models.ImageField()
    phone=models.CharField(max_length=13)
    ish_turi=models.ManyToManyField(Ishturi_or_Bolim)
    id_raqam=models.IntegerField(default=1,unique=True)

    def is_upperclass(self):
        return self.status in {self.gender_female,self.gender_male}

class Xato(models.Model):
    xato_id=models.IntegerField(verbose_name=u"xato id si",unique=True,default=1,null=True,blank=True)
    problem=models.TextField()

    def __str__(self):
        return '{} {}'.format(self.xato_id,self.problem)

class Workinspection(models.Model):
    xodim_id=models.ForeignKey(Xodim,on_delete=models.CASCADE)
    xato_id=models.ForeignKey(Xato,on_delete=models.CASCADE)
    xato_soni=models.PositiveIntegerField(null=True)
    yaroqli_product_soni=models.PositiveIntegerField(null=True)
    ish_vaqti=models.PositiveIntegerField(null=True)
    created=models.DateTimeField(auto_now_add=True, db_comment="Date and time when the article was published",verbose_name=u"vaqt/soat"
)
    updated=models.DateTimeField(auto_now=True,verbose_name=u"vaqtni yangilash")
    # rasm=models.ImageField()
    izoh=models.TextField(null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    mahsulot_id=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
   
    def __str__(self):
        return '{} {}'.format(self.xodim_id,self.izoh[:20])
