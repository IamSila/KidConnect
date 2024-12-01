from django.db import models

# Create your models here.

"""services model"""



"""teams model"""
"""Teams Model"""
class Team(models.Model):
    """creating a model to store the details for the teams sections
    - Full name
    - profile photo
    - position
    - description
    [these will be filled in by the admin for now or we can create a page for that]
    """

    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    profile_photo = models.ImageField(upload_to='profiles')

    def __str__(self):
        """returns the full_name of the object as the name of that object"""
        return f"{self.full_name} ----> {self.position}"


"""portfolio model"""



"""analytics model"""
class Analytic(models.Model):
    reportedChildren = models.IntegerField()
    foundChildren = models.IntegerField()
    missingChildren = models.IntegerField()
    workers = models.IntegerField()


    """defining a name for each entry"""
    def __str__(self):
        return f"analytics {self.id}"

