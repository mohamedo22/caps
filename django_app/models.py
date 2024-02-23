from django.db import models
class users(models.Model):
    email=models.EmailField(max_length=254)
    password=models.TextField()
    def __str__(self) :
        return self.email
class admin(models.Model):
    email=models.EmailField(max_length=254)
    password=models.TextField()
    def __str__(self) :
        return self.email
class flats(models.Model):
    primarykey=models.IntegerField()
    price = models.IntegerField()
    bathroomnumber=models.IntegerField()
    bedroomnumber=models.IntegerField()
    gov = models.TextField()
    city=models.TextField()
    floornumber=models.IntegerField()
    with_f = models.BooleanField()
    active=models.BooleanField()
    phone = models.IntegerField()
class flat_images(models.Model):
    flat = models.ForeignKey(flats, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='flat_images/')
    
