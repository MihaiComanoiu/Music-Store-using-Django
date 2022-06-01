from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

    def __str__(self):
      return str(self.name)

    class Meta:
        verbose_name = 'Categorie'


class Instrument(models.Model):
    name = models.CharField(max_length=30)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='base/images')

    def __str__(self):
      return str(self.name)
