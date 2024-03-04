from django.db import models
class users(models.Model):
    email=models.EmailField(max_length=254)
    password=models.TextField()
    nationalid=models.CharField(max_length=100, null = True)
    def __str__(self) :
        return self.email
class admins_s(models.Model):
    email=models.EmailField(max_length=254)
    password=models.TextField()
    def __str__(self) :
        return self.email
class flats(models.Model):
    price = models.IntegerField()
    bathroomnumber=models.IntegerField()
    bedroomnumber=models.IntegerField()
    gov = models.TextField()
    city=models.TextField()
    floornumber=models.IntegerField()
    with_f = models.BooleanField()
    active=models.BooleanField()
    phone = models.IntegerField()
    mainimage = models.ImageField(upload_to='mainimages/' , null = True)
class flat_images(models.Model):
    flat = models.ForeignKey(flats, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='flat_images/')
class social_house(models.Model):
    title = models.CharField(max_length=100,null=True)
    downpayment = models.IntegerField()
    bathroomnumber=models.IntegerField()
    bedroomnumber=models.IntegerField()
    detiels = models.TextField()
    city=models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    mainimage = models.ImageField(upload_to='social_house_mainimg/' , null = True)
class socialhouse_images(models.Model):
    social_house = models.ForeignKey(social_house, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='social_house_imgs/')