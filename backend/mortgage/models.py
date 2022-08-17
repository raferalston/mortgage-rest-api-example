from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

# Create your models here.


class BankModel(models.Model):
    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'

    bank_name = models.CharField(max_length=50)
    term_min = models.PositiveSmallIntegerField(default=10, validators=[
        MinValueValidator(10),
        MaxValueValidator(30),
        ]
        )
    term_max = models.PositiveSmallIntegerField(default=30, validators=[
        MinValueValidator(10),
        MaxValueValidator(30)]
        )
    rate_min = models.DecimalField(default=1.8, max_digits=2, decimal_places=1)
    rate_max = models.DecimalField(default=9.8, max_digits=2, decimal_places=1)
    payment_min = models.PositiveIntegerField(default=1_000_000, validators=[
        MinValueValidator(1_000_000),
        MaxValueValidator(10_000_000)]
        )
    payment_max = models.PositiveIntegerField(default=10_000_000, validators=[
        MinValueValidator(1_000_000),
        MaxValueValidator(10_000_000)]
        )

    def __str__(self):
        return f'{self.bank_name}'

    def clean(self):
        term_min = self.term_min
        term_max = self.term_max
        if term_min and term_max:
            if term_min > term_max:
                raise ValidationError(
                    "Minimum term must not be greater than maximum"
                )

        rate_min = self.rate_min
        rate_max = self.rate_max
        if rate_min and rate_max:
            if rate_min > rate_max:
                raise ValidationError(
                    "Minimum rate must not be greater than maximum"
                )

        payment_min = self.payment_min
        payment_max = self.payment_max
        if payment_min and payment_max:
            if payment_min > payment_max:
                raise ValidationError(
                    "Minimum payment must not be greater than maximum"
                )
    