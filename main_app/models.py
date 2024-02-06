from django.db import models
from datetime import date


# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# new code above
class Perch(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name


# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    perch = models.ManyToManyField(Perch)

    def feeder_for_today(self):
      return self.feeder_set.filter(date=date.today()).count() >= len(MEALS)

# Add new Feeding model below Cat model
class Feeder(models.Model):
  date = models.DateField('Seen eating at the Feeder')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
  

