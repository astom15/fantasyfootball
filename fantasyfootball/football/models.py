from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

# Create your models here.


class Teams(models.Model):
    team = models.CharField(max_length=30)


class Positions(models.Model):
    position = models.CharField(max_length=20)


class Players(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    games = models.IntegerField()
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)


class Quarterbacks(models.Model):
    yards = models.IntegerField()
    completions = models.IntegerField()
    attempts = models.IntegerField()
    completion_percentage = models.DecimalField(max_digits=3, decimal_places=1)
    touchdowns = models.IntegerField()
    touchdown_percentage = models.DecimalField(max_digits=3, decimal_places=1)
    interceptions = models.IntegerField()
    interception_percentage = models.DecimalField(
        max_digits=3, decimal_places=1)
    first_downs_passing = models.IntegerField()
    longest_completed_pass = models.IntegerField()
    average_yards_per_attempt = models.DecimalField(
        max_digits=3, decimal_places=1)
    adjusted_average_yards_per_attempt = models.DecimalField(
        max_digits=3, decimal_places=1)
    yards_per_completion = models.DecimalField(max_digits=3, decimal_places=1)
    yards_per_game = models.DecimalField(max_digits=3, decimal_places=1)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    times_sacked = models.IntegerField()
    yards_lost_to_sacks = models.IntegerField()
    sack_percentage = models.DecimalField(max_digits=3, decimal_places=1)
    comebacks = models.IntegerField()
    game_winning_drives = models.IntegerField()
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
