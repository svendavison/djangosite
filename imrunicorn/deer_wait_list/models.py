from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from phone_field import PhoneField


class Recipient(models.Model):
    name = models.CharField(max_length=150)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True, max_length=254)
    perceived_thankfulness = models.IntegerField(null=True, blank=True,
                                                 validators=[
                                                     MaxValueValidator(10),
                                                     MinValueValidator(1)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class MeatCut(models.Model):
    name = models.CharField(max_length=150)
    level_of_effort = models.IntegerField(null=True, blank=True,
                                          validators=[
                                              MaxValueValidator(10),
                                              MinValueValidator(1)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Flavor(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class RequestedOrder(models.Model):
    removal_date = models.DateField(default=date.today)
    recipient = models.ForeignKey(Recipient, related_name='recipient', on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavor, related_name='flavor', on_delete=models.CASCADE, null=True)
    choice_cuts = models.ManyToManyField(MeatCut)

    def __str__(self):
        return "%s - %s" % (self.removal_date, self.recipient)

    class Meta:
        ordering = ('removal_date',)
 
