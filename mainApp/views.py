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
        status = request.POST['status']
        #mapping each entry in a new report
        newReport = Report(firstName=firstName, middleName=middleName, lastName=lastName, email=email,\
                           gender=gender, age=age, height=height, skinTone=skinTone, location=location, dressing=dressing,\
                            profilePhoto=profilePhoto, status = status)
        
        newReport.save()

    return render(request, 'report.html')

def base(request):
    """rendering the base file for testing purposes"""
    return render(request, 'base.html')

#reported
def reportedChildren(request):
    """rendering all reported children"""
    context = {}
    reportedChildren = Report.objects.all()
    context['reportedChildren'] =  reportedChildren
    return render(request, 'reportedChildren.html', context)

#search
def search(request):
    """logic for the search bar and button"""
    if request.method == 'GET':
        search = request.GET['search']
        posts = Report.objects.filter(firstName = search)
        return render(request, 'search.html', {'posts':posts})