from django.db import models

#The code to create models is the same regardless of the db chosen for the project

# With models.Model django will save the model onto the db
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


