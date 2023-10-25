from django.db import models

class Products(models.Model):

    CHOICE_TYPE = (
        ('hit', 'Хит'),
        ('all', 'общие'),
        ('sponsor', 'реклама'),
    )

    name = models.CharField(max_length=50, verbose_name="Имя")
    type = models.CharField(max_length=50, choices=CHOICE_TYPE, default='all', verbose_name="Тип")
    price = models.IntegerField(max_length=50, verbose_name="Цена")
    image = models.ImageField(null=True, blank=True, upload_to="image/")

    class Meta:
        
        verbose_name = 'товар'
        verbose_name_plural = 'список товаров'
        

    def __str__(self):
        return self.name