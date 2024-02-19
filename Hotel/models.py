from django.db import models


class Hotel(models.Model):
    RATINGS_HOTEL = (
        ("1", '1 звезд'),
        ("2", '2 звезд'),
        ("3", '3 звезд'),
        ("4", '4 звезд'),
        ("5", '5 звезд'),
    )

    DISCOUNT_PERCENTAGE = (
        ("15", '10%'),
        ("25", '25%'),
        ("35", '35%'),
        ("45", '45%'),
        ("55", '55%'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.URLField(verbose_name="Укажите ссылку на фото",)
    rating = models.CharField(max_length=100, choices=RATINGS_HOTEL)
    address = models.IntegerField()
    email = models.EmailField()
    number = models.IntegerField(blank=True)
    price = models.PositiveIntegerField()
    discount = models.CharField(max_length=100, choices=DISCOUNT_PERCENTAGE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.price}, {self.rating}"
