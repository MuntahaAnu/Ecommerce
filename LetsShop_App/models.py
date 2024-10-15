from django.db import models
from django.contrib.auth.models import User

class Slider(models.Model):
    title = models.CharField(max_length=50)
    title1 = models.CharField(max_length=50)
    description = models.TextField()
    button_tag = models.CharField(max_length=50)
    image = models.ImageField(upload_to='slider_image/')

    def __str__(self):
        return str(self.title)

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.title} , {self.category}')

class Super_SubCategory(models.Model):
    title = models.CharField(max_length=50)
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

class SIZE(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

class COLOR(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

class CONDITION(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

class Product(models.Model):
    
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='slider_image/', null=True, blank=True)
    image1 = models.ImageField(upload_to='slider_image1/', null=True, blank=True)
    image2 = models.ImageField(upload_to='slider_image2/',null=True, blank=True)
    image3 = models.ImageField(upload_to='slider_image3/',null=True, blank=True)
    current_price = models.DecimalField( decimal_places=2, max_digits=10)
    prev_price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.TextField()
    color = models.ManyToManyField(COLOR)
    size= models.ManyToManyField(SIZE)
    top_seller = models.BooleanField(default=False)
    deals_of_the_day = models.BooleanField(default=False)
    trending_product = models.BooleanField(default=False)
    featured_product = models.BooleanField(default=False)
    condition = models.ManyToManyField(CONDITION)
    quantity = models.PositiveIntegerField()
    wish_list = models.BooleanField(default=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    update_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
