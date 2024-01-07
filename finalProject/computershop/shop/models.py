from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
# Create your models here.


class MainCatigeory(models.Model):
    name = models.CharField(max_length=255,null=True)
    slug = models.SlugField(unique=True)
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
class SubCategory(models.Model):
    category = models.ForeignKey(MainCatigeory,on_delete = models.CASCADE)
    subcategory = models.CharField(max_length=255,null=True)
    
    def __str__(self):
        return self.subcategory

class Product(models.Model):
    productTitle = models.ForeignKey(MainCatigeory,on_delete = models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete = models.CASCADE)
    ads = models.CharField(max_length = 255, null=True)
    ProductName = models.CharField(max_length=255,null=True)
    price = models.FloatField(null=True)
    digital = models.BooleanField(default=False, blank=True,null=True)
    image = models.ImageField(upload_to='proudctImages')
    create_date = models.DateField()
    update_date = models.DateTimeField()
    
    def __str__(self):
        return self.ProductName
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url= ''
        return url

class Promotion(models.Model):
    name = models.CharField(max_length = 255,null=True)
    promoPrice = models.IntegerField(null=True)
    advertise = models.CharField(max_length=255,null=True)
    image = models.ImageField(null=True, upload_to='firstPromotion')
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url