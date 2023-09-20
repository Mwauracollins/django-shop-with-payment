from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Electronic', 'Electronic'),
        ('Grocery', 'Grocery'),
        ('Kitchenware', 'Kitchenware'),
    ]
    category = models.CharField(choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products-image')
    slug = models.SlugField(blank=True)

    def __str__(self):
        self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
