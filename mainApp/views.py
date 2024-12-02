from django.shortcuts import render
from . models import Analytic, Team, Report


# Create your views here.
def index(request):
    context = {}
    Analytics = Analytic.objects.all()
    context['analytics'] = Analytics

    """getting all team members"""
    Teams = Team.objects.all()
    context['Teams'] = Teams
    return render(request, 'index.html', context)


#report a missing child
def report(request):
    """define the report.html backend"""
    if request.method == 'POST':
        firstName = request.POST['firstName']
        middleName = request.POST['middleName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        gender = request.POST['gender']
        age = request.POST['age']
        height = request.POST['height']
        skinTone = request.POST['skinTone']
        location = request.POST['location']
        dressing = request.POST['dressing']
        profilePhoto = request.POST['profilePhoto']

        #mapping each entry in a new report
        newReport = Report(firstName=firstName, middleName=middleName, lastName=lastName, email=email,\
                           gender=gender, age=age, height=height, skinTone=skinTone, location=location, dressing=dressing,\
                            profilePhoto=profilePhoto)
        
        newReport.save()

    return render(request, 'report.html')