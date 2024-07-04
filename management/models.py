from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    fees_paid = models.DecimalField(max_digits=10, decimal_places=2)
    fees_pending = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    salary_paid = models.DecimalField(max_digits=10, decimal_places=2)
    salary_needed = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description
