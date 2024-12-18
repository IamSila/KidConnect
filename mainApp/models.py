from django.db import models

# Create your models here.

"""services model"""



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
    customisableImage = models.ImageField(upload_to='media', default='images/happy-family.avif')
    reportedChildren = models.IntegerField()
    foundChildren = models.IntegerField()
    missingChildren = models.IntegerField()
    workers = models.IntegerField()
    year = models.IntegerField(default='2024')


    # defining the name for each entry
    def __str__(self):
        """Each entry will be labelled as shown below"""
        return f"analytics ----> {self.id}"

"""report a case model"""
class Report(models.Model):
    firstName = models.CharField(max_length=256)
    middleName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    height = models.IntegerField()
    skinTone = models.CharField(max_length=50)
    location = models.CharField(max_length=256)
    dressing = models.TextField()
    profilePhoto = models.ImageField(upload_to='media', default="media/media/parent-wife-child.png")
    status = models.CharField(max_length=256, default='pending')

    def __str__(self):
        return f"{self.firstName } {self.lastName}"