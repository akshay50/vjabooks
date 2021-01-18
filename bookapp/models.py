from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

SELLER_CHOICES = ( 
    ("Brainy Bro's Online Services", "Brainy Bro's Online Services"), 
)
DELIVERY_CHOICES = ( 
    ("3-5 Days", "3-5 Days"), 
)

class Author(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CompetitionExam(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


# class Weight(models.Model):
    
#     length = models.PositiveIntegerField(blank=True)
#     breadth = models.PositiveIntegerField(blank=True)
#     height = models.PositiveIntegerField(blank=True)

class Book(models.Model):
    name = models.CharField(max_length=100)
    comingsoon = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    markedprice = models.PositiveIntegerField()
    sellingprice = models.PositiveIntegerField(blank=True)
    codcharge = models.PositiveIntegerField(default='1')
    categories = models.ManyToManyField(Category)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE)
    competitionexam = models.ManyToManyField(CompetitionExam)
    indexsample = models.FileField(upload_to='bookindex/')
    pages = models.PositiveSmallIntegerField()
    coverphoto = models.ImageField(upload_to='coverphoto/')
    seller = models.CharField(max_length=100, choices=SELLER_CHOICES, default='1')
    delivery = models.CharField(max_length=100, choices=DELIVERY_CHOICES, default='1')
    offer = models.PositiveIntegerField(blank=True, default='1')
    note = models.CharField(max_length=100, blank=True)
    buylinkcod = models.URLField(blank=True)
    buylinkonline = models.URLField(default='1')
    stock = models.BooleanField(default=False)
    onboard_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)

    @property
    def prepaid_offer(self):
        return self.sellingprice - self.offer

    @property
    def cod_charge(self):
        return self.sellingprice + self.codcharge

    # @property
    # def offer_price(self):
    #     return self.price_offer 
